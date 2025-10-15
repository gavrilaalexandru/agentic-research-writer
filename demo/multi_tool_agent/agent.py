import os

from google.adk.agents import LlmAgent, Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_FOLDER_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "../../test_research_files"))
if not os.path.isdir(TARGET_FOLDER_PATH):
    print(f"WARNING: The directory '{TARGET_FOLDER_PATH}' does not exist. Please create it.")

research_agent = Agent(
    name='research_agent',
    model="gemini-2.5-flash",
    description=(
        'Specialized agent in web research and local file system access.'
        'Searches for and collect relevant information on any topic on the internet and reads local files.'
    ),
    instruction="""
    You are a research agent specialized in web research and accessing local files. Your tasks are:
    1. Receive a research topic from the coordinator.
    2. Use google_search to find current and relevant information online.
    3. **You can also access a local file system.** Use the `list_directory` and `read_file` tools to find and read relevant local documents.
    4. Collect important data: statistics, facts, trends, and news from both web and local sources..
    5. Summarize the information in a clear and structured format.
    6. Return the results to the coordinator, mentioning your sources (URL or file path).
    
    Example topics and actions:
    - "Latest trends in renewable energy" -> Use `Google Search`.
    - "Summarize the document 'project_notes.txt'" -> Use `read_file` with the path 'project_notes.txt'.
    - "What research files do we have locally?" -> Use `list_directory` with the path '.'.

    Focus on combining information from all available sources for the most comprehensive answer.
    """,
    tools=[
        google_search,
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='npx',
                    args=[
                        "-y",
                        "@modelcontextprotocol/server-filesystem",
                        TARGET_FOLDER_PATH,
                    ],
                ),
            ),
        ),
    ],
)

writer_agent = LlmAgent(
    name='writer_agent',
    model="gemini-2.5-flash",
    description=(
        'Specialized agent in professional writing.'
        'Create well-structured emails, reports, and documents based on information provided.'
    ),
    instruction="""
    You are a writer agent expert in professional communication. Your tasks:
    1. Receive information/data from the coordinator (research results)
    2. Analyze the context and purpose of the communication
    3. Write professional, clear and convincing content

    Types of content you can create:
    - Professional emails (pitch, update, invitation, newsletter)
    - Synthesized reports
    - Informative articles
    - Short presentations
    
    Your style:
    - Professional but accessible
    - Structured (introduction, body, conclusion)
    - Persuasive when appropriate
    - Include data and statistics from the research
    - Add call-to-action when relevant
    
    If you receive data about "AI in healthcare", write a captivating email that:
    - Presents the key findings
    - Is convincing
    - Has a tone appropriate to the context
    """,
)

coordinator_agent = LlmAgent(
    name='coordinator_agent',
    model="gemini-2.5-flash",
    description=(
        'Coordinating agent who manages the complete workflow: '
        'research → writing → delivery. Decides when and how to call each agent.'
    ),
    instruction="""
    You are the coordinator of the multi-agent system. Your role is to orchestrate an efficient workflow:

    STANDARD WORKFLOW:
    When you receive a request like "write a/an [DOCUMENT_TYPE] about [TOPIC]":
    
    STEP 1: Identify the topic
    - Extract the main topic from the user's request
    
    STEP 2: Call research_agent
    - Delegate: "Search for information about [TOPIC]"
    - Wait for the results (data, statistics, facts)
    
    STEP 3: Call writer_agent
    - Delegate: "Write a [DOCUMENT_TYPE] about [TOPIC] using this information: [RESEARCH_RESULTS]"
    - Specify the tone and context
    
    STEP 4: Deliver the final result
    - Present the created email/document
    - Provide editing options if necessary
    
    EXAMPLE REQUESTS:
    User: "Write an email about AI in education"
    → research_agent: search for "AI in education trends 2025"
    → writer_agent: write a professional email with data found
    
    User: "I want a newsletter about solar energy"
    → research_agent: search for "solar energy innovations 2025"
    → writer_agent: create newsletter with the information
    
    DECISION CRITERIA:
    - If the request involves a new/current topic → FIRST research, THEN writing
    - If the user requests changes → only writer_agent
    - If the user wants more information → only research_agent
    
    Be transparent: explain which agent you're using and why.
    """,
    tools=[
        AgentTool(agent=research_agent),
        AgentTool(agent=writer_agent),
    ],
)

root_agent = coordinator_agent