"""Chainlit UI for the Accenture ADM Hierarchical Delivery Crew."""

import chainlit as cl
from dotenv import load_dotenv

load_dotenv()

from crewai.types.streaming import StreamChunkType  # noqa: E402
from accenture_adm_hierarchical_delivery_crew.crew import (  # noqa: E402
    AccentureAdmHierarchicalDeliveryCrew,
)

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


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content=(
            "**Welcome to the Accenture ADM Delivery Crew**\n\n"
            "I'll connect you with our consulting team to help plan and "
            "deliver your engagement. To get started, please tell me:\n\n"
            "1. **Your company name**\n"
            "2. **What type of engagement** you're looking for "
            "(e.g., Digital Transformation, Cloud Migration, ERP Modernization)\n\n"
            "Our team of specialists — from strategy through architecture, "
            "delivery, and deployment — will work through each phase with you. "
            "They may ask you clarifying questions along the way."
        )
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    # Parse client name and engagement type from the message
    user_input = message.content.strip()

    # Ask for structured input if not clear
    session_data = cl.user_session.get("inputs")

    if session_data is None:
        # First message — try to extract client name and engagement type
        res = await cl.AskUserMessage(
            content=f"Thanks! Let me confirm the details.\n\n**What is your company name?**"
        ).send()
        client_name = res["output"].strip() if res else "Client"

        res = await cl.AskUserMessage(
            content=(
                f"Got it — **{client_name}**.\n\n"
                "**What type of engagement are you looking for?**\n\n"
                "Examples: Digital Transformation, Cloud Migration, "
                "ERP Modernization, POS Modernization, Data Platform Build"
            )
        ).send()
        engagement_type = res["output"].strip() if res else "Digital Transformation"

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

        # Run the crew
        await run_crew(inputs)
        return

    # If crew already ran, let user know
    await cl.Message(
        content="The engagement has already been completed. Refresh the page to start a new one."
    ).send()


async def run_crew(inputs: dict):
    """Kick off the crew with streaming output to the Chainlit UI."""
    crew_instance = AccentureAdmHierarchicalDeliveryCrew()
    crew_obj = crew_instance.crew()

    streaming = await crew_obj.kickoff_async(inputs=inputs)

    current_task = None
    current_agent = None
    step = None
    response_msg = None

    async for chunk in streaming:
        task_name = getattr(chunk, "task_name", None)
        agent_role = getattr(chunk, "agent_role", None)

        # When a new task starts, create a new Step and message
        if task_name and task_name != current_task:
            # Close previous message
            if response_msg:
                await response_msg.update()

            current_task = task_name
            current_agent = agent_role

            label = TASK_LABELS.get(task_name, task_name)
            agent_label = agent_role or "Agent"

            # Show phase header
            await cl.Message(
                content=f"### Phase: {label}\n*{agent_label}*",
            ).send()

            # Start fresh message for this phase's output
            response_msg = cl.Message(content="")
            await response_msg.send()

        # Stream text content
        if chunk.chunk_type == StreamChunkType.TEXT:
            if response_msg is None:
                response_msg = cl.Message(content="")
                await response_msg.send()
            await response_msg.stream_token(chunk.content)

        # Show tool usage
        elif chunk.chunk_type == StreamChunkType.TOOL_CALL:
            tool_call = getattr(chunk, "tool_call", None)
            if tool_call:
                tool_name = getattr(tool_call, "tool_name", "tool")
                async with cl.Step(name=f"Using: {tool_name}", type="tool") as tool_step:
                    tool_step.output = f"Called {tool_name}"

    # Final update
    if response_msg:
        await response_msg.update()

    # Completion message
    await cl.Message(
        content=(
            "---\n\n"
            "**Engagement complete.** All ADM phases have been executed.\n\n"
            "The final executive synthesis report has been saved to "
            "`output/engagement_closure_report.md`."
        )
    ).send()
