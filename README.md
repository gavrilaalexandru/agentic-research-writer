# Agentic Research Writer

A multi-agent system built with Google's Agent Development Kit (ADK) that coordinates specialized AI agents to research topics on the web and local files and generate professional content.

**ITSS Back to School 2025 - AI Challenge**

## Overview

This project demonstrates an intelligent multi-agent architecture where:
- A **Coordinator Agent** orchestrates the workflow
- A **Research Agent** searches the web for current information and reads documents from a local file system.
- A **Writer Agent** creates professional emails, newsletters, and documents

The agents collaborate seamlessly to transform user requests into well-researched, professionally written content, drawing from both online and local sources.

## Architecture

```
User Request
    ↓
Coordinator Agent (orchestrator)
    ├──> Research Agent (web search & local file access)
    └──> Writer Agent (content creation)
    ↓
Final Output (email/document)
```

### Agent Details:

**1. Coordinator Agent**
- Analyzes user requests
- Delegates tasks to specialized agents
- Manages the workflow: research → write → deliver

**2. Research Agent**
- Uses Google Search to find current information
- Accesses a local file system to list directories and read files
- Collects data, statistics, and trends
- Returns structured research results

**3. Writer Agent**
- Creates professional content
- Supports: emails, newsletters, reports, articles
- Incorporates research data into compelling narratives

## Windows Installation

### Step 1: Install WSL

```bash
wsl --install
```

For detailed instructions: [Microsoft WSL Installation Guide](https://learn.microsoft.com/en-us/windows/wsl/install)

### Step 2: Install Node.js

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo bash -
sudo apt-get install -y nodejs
```

### Step 3: Install Python 3.12+

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12
sudo apt install python3.12-venv
```

### Step 4: Set Up Virtual Environment

```bash
python3.12 -m venv myenv
source myenv/bin/activate
```

### Step 5: Install Google ADK

```bash
pip install google-adk
```

### Step 6: Get Google API Key

1. Visit [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key)
2. Click "Get a Gemini API key in Google AI Studio"
3. Create and copy your API key

### Step 7: Configure Environment

Create a `.env` file inside `multi_tool_agent/`:

```bash
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here
```

---

## macOS/Linux Installation

### Step 1: Install Node.js

**macOS (using Homebrew):**
```bash
brew install node
```

**Linux:**
```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo bash -
sudo apt-get install -y nodejs
```

### Step 2: Install Python 3.12+

**macOS (using Homebrew):**
```bash
brew install python@3.12
```

**Linux:**
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12
sudo apt install python3.12-venv
```

### Step 3: Set Up Virtual Environment

```bash
python3.12 -m venv myenv
source myenv/bin/activate
```

### Step 4: Install Google ADK

```bash
pip install google-adk
```

### Step 5: Get Google API Key

1. Visit [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key)
2. Click "Get a Gemini API key in Google AI Studio"
3. Create and copy your API key

### Step 6: Configure Environment

Create a `.env` file inside `multi_tool_agent/`:

```bash
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here
```

---

## Project Structure

```
demo/
    multi_tool_agent/
        __init__.py          # Package initializer
        agent.py             # Multi-agent system implementation
        .env                 # Environment configuration
test_research_files/         # Directory for local file research
    project_notes.txt
```

**__init__.py:**
```python
from . import agent
```

**agent.py:** Contains the complete multi-agent implementation (provided in this repository)

## Usage

### Set Up the Research Directory

Before running the application, you must create the directory the research_agent will use.

```bash
mkdir test_research_files
echo "Project Chimera is a multi-agent system focused on Q4 2025 goals." > test_research_files/project_notes.txt
```


### Running the Web Interface

Navigate to the parent directory of your agent folder:

```bash
cd demo
adk web
```

The web interface will start at `http://localhost:8000`

### Running via Command Line

```bash
cd demo
adk run multi_tool_agent
```

## Example Queries

Try these prompts in the chat interface:

**Email Generation:**
```
Write an email about AI in healthcare
```

**Newsletter Creation:**
```
Create a newsletter about solar energy innovations
```

**Local File System Research:**
```
What files are in the local research directory?
Summarize the document 'project_notes.txt' for me.
Write a report based on the information in project_notes.txt.
```

**Research Report:**
```
Write a report on cybersecurity trends for 2025
```

**Custom Request:**
```
Generate a professional email about the impact of AI in education, including recent statistics
```

## Technical Details

### Technologies Used
- **Google ADK**: Agent orchestration framework
- **Gemini 2.5 Flash**: Large language model
- **Google Search**: Built-in web search tool
- **Model Context Protocol (MCP)**: For integrating the local file system tool.
- **Python 3.14**: Implementation language


## Agent Configuration

All agents use the `gemini-2.5-flash` model:

- **Research Agent**: `Agent` type with `google_search` tool and `MCPToolset` for file system access
- **Writer Agent**: `LlmAgent` type for content generation
- **Coordinator Agent**: `LlmAgent` type with `AgentTool` wrappers
