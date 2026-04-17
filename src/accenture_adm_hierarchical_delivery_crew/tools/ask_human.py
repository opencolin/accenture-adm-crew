"""Tool that asks the client questions through the Chainlit UI.

Uses a shared queue so that on_message can route user replies back to the
agent that asked the question, instead of conflicting with AskUserMessage.
"""

import asyncio
import threading

from crewai.tools import BaseTool
from pydantic import BaseModel, Field

# Shared state for coordinating between the ask_human tool (sync, on a crew
# worker thread) and the Chainlit on_message handler (async, on the event loop).
_pending_question: str | None = None
_response_event = threading.Event()
_response_value: str | None = None
_lock = threading.Lock()


def set_pending_question(question: str):
    """Called by the tool to register a question and wait for the answer."""
    global _pending_question, _response_value
    with _lock:
        _pending_question = question
        _response_value = None
        _response_event.clear()


def get_pending_question() -> str | None:
    """Called by on_message to check if an agent is waiting for input."""
    with _lock:
        return _pending_question


def submit_response(answer: str):
    """Called by on_message to deliver the user's reply to the waiting tool."""
    global _response_value, _pending_question
    with _lock:
        _response_value = answer
        _pending_question = None
        _response_event.set()


def wait_for_response(timeout: float = 300.0) -> str | None:
    """Called by the tool to block until the user responds."""
    _response_event.wait(timeout=timeout)
    with _lock:
        return _response_value


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

            # Post the question to the UI
            cl.run_sync(cl.Message(content=question).send())

            # Register and wait for the user's reply via on_message
            set_pending_question(question)
            answer = wait_for_response(timeout=300)

            if answer:
                return answer
            return "The client did not respond within the time limit."
        except Exception:
            # Fallback for non-Chainlit execution (e.g. CLI)
            return input(f"\n[Question for client] {question}\n> ")
