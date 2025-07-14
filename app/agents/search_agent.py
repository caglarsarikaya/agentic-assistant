"""Simple web search agent returning canned results for tests."""
from typing import Any

from app.agents.base import BaseAgent


class SearchAgent(BaseAgent):
    def __init__(self, short_memory, long_memory):
        super().__init__("search", "Web search capabilities", short_memory, long_memory)

    def can_handle(self, task: str) -> bool:
        lowered = task.lower()
        return any(word in lowered for word in ["weather", "search", "pulp fiction"])

    def execute(self, session_id: str, task: str) -> Any:
        self.log(session_id, f"search: {task}")
        if "weather" in task.lower() and "paris" in task.lower():
            result = "Weather in Paris is sunny"
        elif "pulp fiction" in task.lower():
            result = "Pulp Fiction is playing at 8pm"
        else:
            result = "Search results"
        self.log(session_id, f"search result: {result}")
        return result
