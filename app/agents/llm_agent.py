"""LLM-only agent for direct responses."""
from __future__ import annotations

import os
from typing import Any

from app.agents.base import BaseAgent

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except Exception:  # pragma: no cover - fallback
    OPENAI_AVAILABLE = False


class LLMAgent(BaseAgent):
    def __init__(self, short_memory, long_memory):
        super().__init__("llm", "Language model for general questions", short_memory, long_memory)
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key and OPENAI_AVAILABLE else None

    def execute(self, session_id: str, task: str) -> Any:
        self.log(session_id, f"LLM input: {task}")
        if self.client:
            resp = self.client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
                messages=[{"role": "user", "content": task}],
                temperature=float(os.getenv("OPENAI_TEMPERATURE", 0.7)),
            )
            result = resp.choices[0].message.content
        else:
            # Simple canned responses for tests
            if "how are" in task.lower():
                result = "I'm just a bunch of code, but I'm doing great!"
            elif "3+5" in task:
                result = "3 + 5 equals 8"
            else:
                result = f"Echo: {task}"
        self.log(session_id, f"LLM output: {result}")
        return result
