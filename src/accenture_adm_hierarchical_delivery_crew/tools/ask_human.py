"""Tool that asks the client questions through the Chainlit UI."""

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class AskHumanInput(BaseModel):
    """Input schema for AskHuman tool."""

    question: str = Field(
        ..., description="The question to ask the client. Be specific and clear."
    )


class AskHumanTool(BaseTool):
    name: str = "Ask Client"
    description: str = (
        "Use this tool to ask the client a question when you need clarification, "
        "requirements details, preferences, or approval. The client will see your "
        "question in the chat UI and respond directly."
    )
    args_schema: type[BaseModel] = AskHumanInput

    def _run(self, question: str) -> str:
        try:
            import chainlit as cl

            response = cl.run_sync(
                cl.AskUserMessage(content=question, timeout=300).send()
            )
            if response:
                return response["output"]
            return "The client did not respond."
        except Exception:
            # Fallback for non-Chainlit execution (e.g. CLI)
            return input(f"\n[Question for client] {question}\n> ")
