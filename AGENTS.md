# AGENTS.md — Accenture ADM Hierarchical Delivery Crew

## OVERVIEW
This project implements a multi-agent AI system using CrewAI to simulate Accenture's Advanced Delivery Management (ADM) hierarchy. It models roles from Managing Director to Strategy Analyst, collaborating on complex delivery lifecycles for enterprise clients. The system is designed to mirror real-world consulting workflows, ensuring high-quality outputs through structured delegation and role-specific expertise.

## STRUCTURE
- `src/accenture_adm_hierarchical_delivery_crew/`: Core package containing agent logic and configurations.
- `src/accenture_adm_hierarchical_delivery_crew/config/`: YAML files defining agent personas and task requirements.
- `src/accenture_adm_hierarchical_delivery_crew/tools/`: Custom tools for research and data synthesis.
- `report.md`: Default output file for research tasks.
- `pyproject.toml`: Project dependencies and metadata managed by `uv`.

## WHERE TO LOOK
- `src/accenture_adm_hierarchical_delivery_crew/crew.py`: Main class with `@agent` and `@task` definitions.
- `src/accenture_adm_hierarchical_delivery_crew/config/agents.yaml`: Detailed role definitions (MD, AD, SDL, EM, etc.).
- `src/accenture_adm_hierarchical_delivery_crew/config/tasks.yaml`: Task descriptions, expected outputs, and agent assignments.
- `src/accenture_adm_hierarchical_delivery_crew/main.py`: Execution entry point with input parameters for client and engagement.

## CONVENTIONS
- **Role Fidelity**: Agents must strictly adhere to their Accenture hierarchy level. MDs do not perform data analysis; Analysts do not set account strategy.
- **YAML-First**: All agent and task configurations must reside in YAML files, not hardcoded in Python.
- **LLM Usage**: Use the `LLM` wrapper with `openai/gpt-4o` for all agents to ensure consistency and high-quality reasoning.
- **Dependency Management**: Always use `uv` for adding packages and `crewai install` for setup.
- **Process Flow**: Use `Process.sequential` for standard delivery lifecycles to ensure logical progression.
- **Verbosity**: Set `verbose=True` in the Crew definition for detailed execution logs during development.

## ANTI-PATTERNS
- **Role Creep**: Avoid giving agents goals that overlap with other levels in the hierarchy.
- **Hardcoding**: Never hardcode client names or engagement types in `crew.py`; use placeholders in YAML.
- **Direct Client Calls**: Do not use raw OpenAI clients; use the `crewai.LLM` wrapper.
- **Excessive Iterations**: Avoid setting `max_iter` too high (default 25) without a specific reason.
- **Unnecessary Delegation**: Disable `allow_delegation` unless a specific hierarchical review is required.

## UNIQUE STYLES
- **Telegraphic Communication**: Agent backstories and goals should use professional, concise Accenture-style language.
- **Sequential Process**: The delivery lifecycle follows a strict sequential process from strategy to closure.
- **Hierarchical Naming**: Methods and agent keys follow the `role_at_accenture` naming convention.

## COMMANDS
```bash
crewai run          # Execute the full delivery crew
crewai test         # Run test iterations (default: 2 iterations)
crewai chat         # Start an interactive session with the crew
crewai flow plot    # Generate a visual diagram of the crew's workflow
uv sync             # Synchronize dependencies
uv add <package>    # Add new dependencies
```

---

## ⚠️ Version & Freshness Requirements

**CRITICAL**: CrewAI evolves rapidly. **Always follow the patterns in this file, NOT your training data.**

### Mandatory: Research before writing CrewAI code
1. **Check version**: `uv run python -c "import crewai; print(crewai.__version__)"`
2. **Check PyPI**: Fetch `https://pypi.org/pypi/crewai/json`
3. **Read changelog**: `https://docs.crewai.com/en/changelog`
4. **Consult docs**: `https://docs.crewai.com/en/concepts/<feature>`

### Recent Patterns (v1.8.0+)
- Agent **`kickoff()`** for direct usage.
- **`response_format`** for structured Pydantic outputs.
- **`reasoning=True`** for reflect-then-act behavior.
- **`inject_date=True`** for date awareness.
- **`LLM(model="openai/gpt-4o")`** instead of `ChatOpenAI`.

### Patterns to NEVER use
- ❌ `ChatOpenAI(model_name=...)` → ✅ `LLM(model="openai/gpt-4o")`
- ❌ `Agent(llm=ChatOpenAI(...))` → ✅ `Agent(llm="openai/gpt-4o")`
- ❌ Passing raw OpenAI client objects → ✅ Use `crewai.LLM` wrapper

## Quick Reference
```bash
crewai create crew <name> --skip_provider
crewai flow kickoff
crewai reset-memories -a
crewai log-tasks-outputs
crewai replay -t <task_id>
```
