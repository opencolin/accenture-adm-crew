# Accenture ADM Hierarchical Delivery Crew

A multi-agent AI system that simulates Accenture's Application Delivery Method (ADM) lifecycle. Built with [CrewAI](https://crewai.com) and powered by [Nebius Token Factory](https://tokenfactory.nebius.com) inference.

## Executive Summary

This project deploys 11 AI agents — each representing a distinct Accenture delivery role — to collaboratively execute a full enterprise engagement lifecycle. A Managing Director agent orchestrates the crew hierarchically, delegating work across strategy, consulting, architecture, development, testing, and deployment phases.

The system accepts a client name and engagement type as input and produces structured deliverables across 12 ADM phases: from initial engagement strategy through solution architecture, sprint execution, UAT coordination, production deployment, and executive closure.

A Chainlit web UI enables real-time client interaction: clients describe their project, watch the crew work through each phase with streaming output, and answer clarifying questions from the consulting team directly in the chat.

**Key capabilities:**
- Hierarchical agent orchestration with delegation across 11 specialist roles
- 12-phase ADM lifecycle execution with task dependencies and context passing
- Interactive client-facing chat UI with human-in-the-loop questioning
- Web search (Tavily) and site scraping tools for real-world research
- Streaming output with per-phase progress visualization
- Final executive synthesis report generated as a deliverable

**Tech stack:** CrewAI 1.13 | DeepSeek V3.2 via Nebius Token Factory | Tavily Search | Chainlit | Python 3.11+

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Chainlit Web UI                        │
│              Client chat + streaming output                 │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              Managing Director (Manager Agent)              │
│         Orchestrates all tasks hierarchically               │
│                   DeepSeek V3.2                             │
└───────────────────────┬─────────────────────────────────────┘
                        │ delegates to
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  Strategy &  │ │  Technology  │ │  Delivery &  │
│  Consulting  │ │     Track    │ │  Operations  │
│              │ │              │ │              │
│ • Assoc Dir  │ │ • Solution   │ │ • Sr Delivery│
│ • Engagement │ │   Architect  │ │   Lead       │
│   Manager    │ │ • Technology │ │ • Program    │
│ • Mgmt       │ │   Architect  │ │   Mgmt Lead  │
│   Consultant │ │ • Tech       │ │ • Digital PM │
│ • Strategy   │ │   Delivery   │ │              │
│   Analyst    │ │   Lead       │ │              │
└──────────────┘ └──────────────┘ └──────────────┘
        │               │               │
        ▼               ▼               ▼
   ┌─────────┐    ┌─────────┐    ┌─────────┐
   │ Tavily  │    │ Tavily  │    │ Tavily  │
   │ Search  │    │ Search  │    │ Search  │
   │ Scrape  │    │ Scrape  │    │ Scrape  │
   │ Ask     │    │         │    │         │
   │ Client  │    │         │    │         │
   └─────────┘    └─────────┘    └─────────┘
```

## ADM Phases

The crew executes 12 tasks in sequence, each assigned to a specialist agent. Tasks receive context from their predecessors, building a coherent engagement narrative.

| # | Phase | Agent | Tools |
|---|-------|-------|-------|
| 1 | Engagement Strategy & Delivery Planning | Associate Director | Search, Scrape, Ask Client |
| 2 | Strategic Engagement Approval | Senior Delivery Lead | Search, Scrape, Ask Client |
| 3 | Business Requirements Analysis | Strategy & Consulting Analyst | Search, Scrape, Ask Client |
| 4 | Backlog Definition & Scope Planning | Management Consultant | Search, Scrape, Ask Client |
| 5 | Solution Architecture Design | Solution Architect | Search, Scrape |
| 6 | Technical Architecture Review | Technology Architect | Search, Scrape |
| 7 | Solution Development & Implementation | Technology Delivery Lead | Search, Scrape |
| 8 | Sprint Execution & Project Tracking | Digital Project Manager | Search, Scrape |
| 9 | Integrated Testing & Solution Validation | Engagement Manager | Search, Scrape, Ask Client |
| 10 | User Acceptance Testing Coordination | Engagement Manager | Search, Scrape, Ask Client |
| 11 | Production Deployment & Cutover | Program Management Lead | Search, Scrape |
| 12 | Service Introduction & Engagement Closure | Associate Director | Search, Scrape, Ask Client |

The final task receives context from all 11 preceding phases to produce a comprehensive executive synthesis report.

## Project Structure

```
├── app.py                                          # Chainlit web UI entry point
├── pyproject.toml                                  # Project config & dependencies
├── .env                                            # API keys (not committed)
├── .chainlit/config.toml                           # Chainlit UI configuration
└── src/accenture_adm_hierarchical_delivery_crew/
    ├── crew.py                                     # Crew orchestration & agent definitions
    ├── main.py                                     # CLI entry point
    ├── config/
    │   ├── agents.yaml                             # Agent roles, goals, backstories
    │   └── tasks.yaml                              # Task descriptions, outputs, dependencies
    └── tools/
        ├── __init__.py
        └── ask_human.py                            # Human-in-the-loop tool (Chainlit integration)
```

## Setup

### Prerequisites

- Python 3.11+ (3.13 recommended)
- [uv](https://docs.astral.sh/uv/) for dependency management
- A [Nebius Token Factory](https://studio.nebius.ai/) API key
- A [Tavily](https://tavily.com/) API key

### Installation

```bash
# Clone the repo
git clone https://github.com/colygon/accenture-adm-crew.git
cd accenture-adm-crew

# Create venv and install dependencies
uv venv --python 3.13
uv sync
uv pip install chainlit tavily-python
```

### Configuration

Create a `.env` file in the project root:

```env
NEBIUS_API_KEY=your_nebius_token_factory_key
TAVILY_API_KEY=your_tavily_api_key
```

## Usage

### Web UI (Chainlit)

```bash
.venv/bin/chainlit run app.py
```

Opens at `http://localhost:8000`. Enter your company name and engagement type, then interact with the consulting team as they work through each ADM phase.

### CLI

```bash
# Interactive prompts for client name and engagement type
.venv/bin/python -m accenture_adm_hierarchical_delivery_crew.main run

# Or via CrewAI CLI
crewai run
```

### Training & Replay

```bash
# Train the crew over N iterations
.venv/bin/python -m accenture_adm_hierarchical_delivery_crew.main train <n_iterations> <output_file>

# Replay from a specific task
.venv/bin/python -m accenture_adm_hierarchical_delivery_crew.main replay <task_id>
```

## Model Configuration

All agents use **DeepSeek V3.2** via Nebius Token Factory (`$0.30/$0.45 per 1M tokens`). The model is configured in `crew.py`:

```python
default_llm = LLM(
    model="openai/deepseek-ai/DeepSeek-V3.2",
    base_url="https://api.tokenfactory.nebius.com/v1",
    api_key=NEBIUS_API_KEY,
)
```

To use a different model, swap the model ID. Available options include:

| Model | Type | Cost (in/out per 1M) |
|-------|------|---------------------|
| `deepseek-ai/DeepSeek-V3.2` | Chat | $0.30 / $0.45 |
| `Qwen/Qwen3.5-397B-A17B` | Chat | $0.60 / $3.60 |
| `zai-org/GLM-5` | Chat | $1.00 / $3.20 |
| `deepseek-ai/DeepSeek-R1-0528` | Reasoning | $0.80 / $2.40 |
| `NousResearch/Hermes-4-405B` | Reasoning | $1.00 / $3.00 |

All model IDs must be prefixed with `openai/` for litellm routing (e.g., `openai/deepseek-ai/DeepSeek-V3.2`).

## Deliverables

Each ADM phase writes its output to `deliverables/` as a numbered markdown file:

| File | Content |
|------|---------|
| `01_engagement_strategy.md` | Engagement strategy & delivery planning |
| `02_strategic_approval.md` | Go/no-go approval decision |
| `03_business_requirements.md` | Functional & non-functional requirements |
| `04_backlog_scope.md` | Prioritized backlog with acceptance criteria |
| `05_solution_architecture.md` | End-to-end architecture design |
| `06_technical_architecture_review.md` | Architecture validation & risk assessment |
| `07_development_implementation.md` | Solution increment & build artifacts |
| `08_sprint_execution.md` | Sprint metrics & progress tracking |
| `09_testing_validation.md` | Test coverage & release readiness |
| `10_uat_coordination.md` | User acceptance testing results |
| `11_deployment_cutover.md` | Go-live execution & stability metrics |
| `12_engagement_closure.md` | Executive synthesis & strategic recommendations |

In the Chainlit UI, deliverables are viewable and downloadable after the engagement completes. Type a number to view a specific deliverable or **all** to browse everything.

## License

Private repository. All rights reserved.
