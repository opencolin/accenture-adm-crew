"""Chainlit UI for the Accenture ADM Hierarchical Delivery Crew."""

from pathlib import Path

import chainlit as cl
from dotenv import load_dotenv

load_dotenv()

from crewai.types.streaming import StreamChunkType  # noqa: E402
from accenture_adm_hierarchical_delivery_crew.crew import (  # noqa: E402
    AccentureAdmHierarchicalDeliveryCrew,
    DEFAULT_MODEL,
)

DELIVERABLES_DIR = Path("deliverables")

TASK_LABELS = {
    "engagement_strategy_delivery_planning": "Engagement Strategy & Delivery Planning",
    "strategic_engagement_approval": "Strategic Engagement Approval",
    "business_requirements_analysis": "Business Requirements Analysis",
    "backlog_definition_scope_planning": "Backlog Definition & Scope Planning",
    "solution_architecture_design": "Solution Architecture Design",
    "technical_architecture_review": "Technical Architecture Review",
    "solution_development_implementation": "Solution Development & Implementation",
    "sprint_execution_project_tracking": "Sprint Execution & Project Tracking",
    "integrated_testing_solution_validation": "Integrated Testing & Solution Validation",
    "user_acceptance_testing_coordination": "User Acceptance Testing Coordination",
    "production_deployment_cutover": "Production Deployment & Cutover",
    "service_introduction_engagement_closure": "Service Introduction & Engagement Closure",
}

DELIVERABLE_NAMES = {
    "01_engagement_strategy.md": "Engagement Strategy",
    "02_strategic_approval.md": "Strategic Approval",
    "03_business_requirements.md": "Business Requirements",
    "04_backlog_scope.md": "Backlog & Scope",
    "05_solution_architecture.md": "Solution Architecture",
    "06_technical_architecture_review.md": "Technical Architecture Review",
    "07_development_implementation.md": "Development & Implementation",
    "08_sprint_execution.md": "Sprint Execution",
    "09_testing_validation.md": "Testing & Validation",
    "10_uat_coordination.md": "UAT Coordination",
    "11_deployment_cutover.md": "Deployment & Cutover",
    "12_engagement_closure.md": "Engagement Closure",
}


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content=(
            "**Welcome to the Accenture ADM Delivery Crew**\n\n"
            "I'll connect you with our consulting team to help plan and "
            "deliver your engagement.\n\n"
            "To get started, **what is your company name?**"
        )
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    # If crew already completed, handle deliverable viewing
    if cl.user_session.get("crew_done"):
        await handle_deliverable_request(message.content.strip())
        return

    if cl.user_session.get("inputs") is not None:
        await cl.Message(content="The crew is still running. Please wait.").send()
        return

    # Step 1: Client name
    client_name = cl.user_session.get("client_name")
    if client_name is None:
        client_name = message.content.strip() or "Client"
        cl.user_session.set("client_name", client_name)
        await cl.Message(
            content=(
                f"Got it — **{client_name}**.\n\n"
                "**What type of engagement are you looking for?**\n\n"
                "Examples: Digital Transformation, Cloud Migration, "
                "ERP Modernization, POS Modernization, Data Platform Build"
            )
        ).send()
        return

    # Step 2: Engagement type → kick off crew
    engagement_type = message.content.strip() or "Digital Transformation"
    inputs = {
        "client_name": client_name,
        "engagement_type": engagement_type,
    }
    cl.user_session.set("inputs", inputs)

    await cl.Message(
        content=(
            f"Starting the **{engagement_type}** engagement for **{client_name}**.\n\n"
            "Our team is assembling now. You'll see each phase as it progresses, "
            "and team members may ask you questions directly.\n\n"
            "---"
        )
    ).send()

    await run_crew(inputs)


async def run_crew(inputs: dict):
    """Kick off the crew with streaming output to the Chainlit UI."""
    crew_instance = AccentureAdmHierarchicalDeliveryCrew()
    crew_obj = crew_instance.crew()

    streaming = await crew_obj.kickoff_async(inputs=inputs)

    current_task = None
    response_msg = None

    async for chunk in streaming:
        task_name = getattr(chunk, "task_name", None)
        agent_role = getattr(chunk, "agent_role", None)

        if task_name and task_name != current_task:
            if response_msg:
                await response_msg.update()

            current_task = task_name
            label = TASK_LABELS.get(task_name, task_name)
            agent_label = agent_role or "Agent"

            await cl.Message(
                content=f"### Phase: {label}\n*{agent_label}*",
            ).send()

            response_msg = cl.Message(content="")
            await response_msg.send()

        if chunk.chunk_type == StreamChunkType.TEXT:
            if response_msg is None:
                response_msg = cl.Message(content="")
                await response_msg.send()
            await response_msg.stream_token(chunk.content)

        elif chunk.chunk_type == StreamChunkType.TOOL_CALL:
            tool_call = getattr(chunk, "tool_call", None)
            if tool_call:
                tool_name = getattr(tool_call, "tool_name", "tool")
                async with cl.Step(name=f"Using: {tool_name}", type="tool") as tool_step:
                    tool_step.output = f"Called {tool_name}"

    if response_msg:
        await response_msg.update()

    cl.user_session.set("crew_done", True)
    await show_deliverables_menu()


async def show_deliverables_menu():
    """Show the list of available deliverables after crew completion."""
    files = sorted(DELIVERABLES_DIR.glob("*.md")) if DELIVERABLES_DIR.exists() else []

    if not files:
        await cl.Message(
            content="---\n\n**Engagement complete.** No deliverable files were generated."
        ).send()
        return

    lines = ["---\n\n**Engagement complete.** All ADM phases have been executed.\n"]
    lines.append("### Deliverables\n")
    lines.append("Type a number to view a deliverable, or **all** to view everything.\n")

    for i, f in enumerate(files, 1):
        label = DELIVERABLE_NAMES.get(f.name, f.stem.replace("_", " ").title())
        lines.append(f"**{i}.** {label}")

    await cl.Message(content="\n".join(lines)).send()


async def handle_deliverable_request(user_input: str):
    """Handle user requests to view deliverables."""
    files = sorted(DELIVERABLES_DIR.glob("*.md")) if DELIVERABLES_DIR.exists() else []

    if not files:
        await cl.Message(content="No deliverables found.").send()
        return

    if user_input.lower() == "all":
        for f in files:
            await send_deliverable(f)
        return

    try:
        idx = int(user_input) - 1
        if 0 <= idx < len(files):
            await send_deliverable(files[idx])
            return
    except ValueError:
        pass

    for f in files:
        label = DELIVERABLE_NAMES.get(f.name, f.stem)
        if user_input.lower() in label.lower() or user_input.lower() in f.name.lower():
            await send_deliverable(f)
            return

    await cl.Message(
        content=f"Couldn't find \"{user_input}\". Type a number (1-{len(files)}) or **all**."
    ).send()


async def send_deliverable(filepath: Path):
    """Send a deliverable file as a viewable message with download option."""
    content = filepath.read_text()
    label = DELIVERABLE_NAMES.get(filepath.name, filepath.stem.replace("_", " ").title())

    await cl.Message(
        content=f"### {label}\n\n{content}",
        elements=[
            cl.File(
                name=filepath.name,
                path=str(filepath.resolve()),
                display="side",
            )
        ],
    ).send()
