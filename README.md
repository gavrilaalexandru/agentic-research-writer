# multi-agent-email-generator

## Workflow Overview

```mermaid
flowchart TD
    A[User Request] --> B[Coordinator Agent]
    B --> C[Research Agent<br/>(searches the web)]
    C --> D[Writer Agent<br/>(writes email/document)]
    D --> E[Final Output]
