"""WhatsApp messaging agent placeholder."""
from typing import Any

from app.agents.base import BaseAgent


class WhatsAppAgent(BaseAgent):
    def __init__(self, short_memory, long_memory):
        super().__init__("whatsapp", "Send messages via WhatsApp", short_memory, long_memory)

    def execute(self, session_id: str, task: str) -> Any:
        self.log(session_id, f"whatsapp: {task}")
        result = "Message sent via WhatsApp"
        self.log(session_id, f"whatsapp result: {result}")
        return result
