# multi-agent-email-generator

## Workflow Overview

```mermaid
flowchart TD
    A[User Request] --> B[Coordinator Agent]
    B --> C[Research Agent\n(searches the web)]
    C --> D[Writer Agent\n(writes email/document)]
    D --> E[Final Output]
