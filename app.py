"""Chainlit UI for the Accenture ADM Hierarchical Delivery Crew."""

import chainlit as cl
from dotenv import load_dotenv

load_dotenv()

from crewai.types.streaming import StreamChunkType  # noqa: E402
from accenture_adm_hierarchical_delivery_crew.crew import (  # noqa: E402
    AccentureAdmHierarchicalDeliveryCrew,
    AVAILABLE_MODELS,
    DEFAULT_MODEL,
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

MODEL_INFO = {
    "DeepSeek V3.2": {"type": "Chat", "cost": "$0.30 / $0.45"},
    "DeepSeek R1": {"type": "Reasoning", "cost": "$0.80 / $2.40"},
    "Qwen 3.5 397B": {"type": "Chat", "cost": "$0.60 / $3.60"},
    "Qwen3 Coder 480B": {"type": "Chat", "cost": "$0.40 / $1.80"},
    "Qwen3 235B Instruct": {"type": "Chat", "cost": "$0.20 / $0.60"},
    "Qwen3 235B Thinking": {"type": "Reasoning", "cost": "$0.20 / $0.80"},
    "GLM-5": {"type": "Chat", "cost": "$1.00 / $3.20"},
    "GLM-4.7": {"type": "Chat", "cost": "$0.40 / $2.00"},
    "Hermes 4 405B": {"type": "Reasoning", "cost": "$1.00 / $3.00"},
    "GPT-OSS 120B": {"type": "Reasoning", "cost": "$0.15 / $0.60"},
    "Kimi K2.5": {"type": "Chat", "cost": "$0.50 / $2.50"},
    "MiniMax M2.5": {"type": "Chat", "cost": "$0.30 / $1.20"},
    "Nemotron 3 Super 120B": {"type": "Chat", "cost": "$0.30 / $0.90"},
    "Llama 3.3 70B": {"type": "Chat", "cost": "$0.13 / $0.40"},
    "Gemma 3 27B": {"type": "Chat", "cost": "$0.10 / $0.30"},
}


@cl.on_chat_start
async def on_chat_start():
    # Build model list for display
    model_lines = []
    for name in AVAILABLE_MODELS:
        info = MODEL_INFO.get(name, {})
        mtype = info.get("type", "Chat")
        cost = info.get("cost", "—")
        marker = " *(default)*" if name == DEFAULT_MODEL else ""
        model_lines.append(f"- **{name}**{marker} — {mtype}, {cost} per 1M tokens")

    model_list = "\n".join(model_lines)

    await cl.Message(
        content=(
            "**Welcome to the Accenture ADM Delivery Crew**\n\n"
            "I'll connect you with our consulting team to help plan and "
            "deliver your engagement.\n\n"
            "First, choose an AI model to power the team. "
            "All models are served via Nebius Token Factory.\n\n"
            f"{model_list}\n\n"
            "Type a model name to select it, or press Enter for the default."
        )
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    session_data = cl.user_session.get("inputs")

    if session_data is not None:
        await cl.Message(
            content="The engagement has already been completed. Refresh the page to start a new one."
        ).send()
        return

    # Step 1: Model selection (if not done yet)
    selected_model = cl.user_session.get("model")
    if selected_model is None:
        user_input = message.content.strip()

        if user_input == "" or user_input.lower() in ("default", "enter"):
            selected_model = DEFAULT_MODEL
        else:
            # Fuzzy match: find the best matching model name
            matched = None
            for name in AVAILABLE_MODELS:
                if user_input.lower() in name.lower():
                    matched = name
                    break
            if matched:
                selected_model = matched
            else:
                await cl.Message(
                    content=f"Model \"{user_input}\" not found. Please pick from the list above, or type **default**."
                ).send()
                return

        cl.user_session.set("model", selected_model)
        info = MODEL_INFO.get(selected_model, {})
        await cl.Message(
            content=(
                f"Using **{selected_model}** ({info.get('type', 'Chat')}, {info.get('cost', '—')}/1M tokens).\n\n"
                "Now let's set up your engagement.\n\n"
                "**What is your company name?**"
            )
        ).send()
        return

    # Step 2: Client name
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

    # Step 3: Engagement type → kick off crew
    engagement_type = message.content.strip() or "Digital Transformation"
    inputs = {
        "client_name": client_name,
        "engagement_type": engagement_type,
    }
    cl.user_session.set("inputs", inputs)

    await cl.Message(
        content=(
            f"Starting the **{engagement_type}** engagement for **{client_name}** "
            f"powered by **{selected_model}**.\n\n"
            "Our team is assembling now. You'll see each phase as it progresses, "
            "and team members may ask you questions directly.\n\n"
            "---"
        )
    ).send()

    await run_crew(inputs, selected_model)


async def run_crew(inputs: dict, model_name: str):
    """Kick off the crew with streaming output to the Chainlit UI."""
    crew_instance = AccentureAdmHierarchicalDeliveryCrew().set_model(model_name)
    crew_obj = crew_instance.crew()

    streaming = await crew_obj.kickoff_async(inputs=inputs)

    current_task = None
    response_msg = None

    async for chunk in streaming:
        task_name = getattr(chunk, "task_name", None)
        agent_role = getattr(chunk, "agent_role", None)

        # When a new task starts, create a new Step and message
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

    if response_msg:
        await response_msg.update()

    await cl.Message(
        content=(
            "---\n\n"
            "**Engagement complete.** All ADM phases have been executed.\n\n"
            "The final executive synthesis report has been saved to "
            "`output/engagement_closure_report.md`."
        )
    ).send()
