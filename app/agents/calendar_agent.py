"""Calendar agent returning canned responses."""
from typing import Any

from app.agents.base import BaseAgent


class CalendarAgent(BaseAgent):
    def __init__(self, short_memory, long_memory):
        super().__init__("calendar", "Google Calendar integration", short_memory, long_memory)

    def can_handle(self, task: str) -> bool:
        lowered = task.lower()
        return any(word in lowered for word in ["calendar", "event", "reminder"])

    def execute(self, session_id: str, task: str) -> Any:
        self.log(session_id, f"calendar: {task}")
        result = "Event created in calendar"
        self.log(session_id, f"calendar result: {result}")
        return result
