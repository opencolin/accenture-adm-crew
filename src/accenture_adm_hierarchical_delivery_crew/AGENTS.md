# AGENTS.md — Accenture ADM Delivery Crew Core

## OVERVIEW
This subdirectory contains the core logic and configurations for the Accenture ADM Hierarchical Delivery Crew. It defines the agents, tasks, and the crew assembly process following Accenture's delivery standards. The implementation focuses on a 11-role hierarchy that covers the entire delivery lifecycle from strategy to service introduction.

## STRUCTURE
- `config/agents.yaml`: Personas, goals, and backstories for all 11 Accenture roles (MD, AD, SDL, EM, PML, MC, SCA, SA, TA, TDL, DPM).
- `config/tasks.yaml`: Sequential delivery lifecycle tasks including strategy, requirements, architecture, development, and testing.
- `crew.py`: The `@CrewBase` implementation that wires agents and tasks together using decorators.
- `main.py`: Entry point for kicking off the crew with client-specific inputs like `client_name` and `engagement_type`.
- `tools/custom_tool.py`: Placeholder for custom tools specific to this crew's delivery requirements.

## WHERE TO LOOK
- **Agent Definitions**: `crew.py` methods decorated with `@agent`. Each method returns an `Agent` instance with role-specific tools.
- **Task Definitions**: `crew.py` methods decorated with `@task`. Each method returns a `Task` instance linked to the YAML config.
- **Role Details**: `config/agents.yaml` for specific Accenture role attributes and backstories.
- **Execution Logic**: `main.py` for how the crew is instantiated and kicked off.

## CONVENTIONS
- **Decorator Usage**: Always use `@agent` and `@task` to allow CrewAI to auto-manage instances and dependencies.
- **Tool Integration**: Assign tools like `SerperDevTool` or `ScrapeWebsiteTool` within the `@agent` methods to maintain encapsulation.
- **Input Placeholders**: Use `{client_name}` and `{engagement_type}` in YAML configs for dynamic injection during kickoff.
- **Agent Config**: Set `reasoning=False` by default unless complex multi-step reflection is required for a specific role.
- **Date Awareness**: Ensure `inject_date=True` is set for all agents to provide temporal context for delivery planning.

## ANTI-PATTERNS
- **Logic in YAML**: Keep YAML files focused on descriptive data; move complex logic to `crew.py` or custom tools.
- **Missing Docstrings**: All `@agent` and `@task` methods should have clear docstrings to help AI assistants understand the intent.
- **Manual Instantiation**: Do not manually create `Agent` or `Task` objects outside the decorated methods in `crew.py`.
- **Tool Overload**: Avoid assigning too many tools to a single agent; keep them focused on their specific role's needs.

## UNIQUE STYLES
- **Accenture Naming**: Methods and agent keys follow the `role_at_accenture` naming convention (e.g., `managing_director_at_accenture`).
- **Sequential Process**: The crew is configured with `Process.sequential` to mirror the strict ADM delivery lifecycle.
- **Role-Specific Tools**: Strategy roles use search tools, while Architect roles use scraping tools for technical research.

## COMMANDS
```bash
# Run from the project root
crewai run

# Run specific tests for this crew
crewai test
```
