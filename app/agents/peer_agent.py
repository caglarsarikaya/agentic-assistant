"""Simple rule-based planner that routes tasks to other agents."""
from typing import Any, Dict, List

from app.agents.base import BaseAgent


class PeerAgent(BaseAgent):
    def __init__(self, short_memory, long_memory, agents: List[BaseAgent]):
        super().__init__("peer", "Planner and router", short_memory, long_memory)
        # Map agent name to instance
        self.agents: Dict[str, BaseAgent] = {agent.name: agent for agent in agents}

    def execute(self, session_id: str, task: str) -> Any:
        self.log(session_id, f"planner received: {task}")
        chosen_agents = self.plan(task)
        results = {}
        for agent in chosen_agents:
            results[agent.name] = agent.execute(session_id, task)
        self.log(session_id, f"planner results: {results}")
        return results

    def plan(self, task: str) -> List[BaseAgent]:
        lowered = task.lower()
        agents = []
        if any(word in lowered for word in ["weather", "search"]):
            if "search" in self.agents:
                agents.append(self.agents["search"])
        if any(word in lowered for word in ["calendar", "event"]):
            if "calendar" in self.agents:
                agents.append(self.agents["calendar"])
        if any(word in lowered for word in ["text", "message", "whatsapp"]):
            if "whatsapp" in self.agents:
                agents.append(self.agents["whatsapp"])
        if not agents:
            agents.append(self.agents.get("llm"))
        else:
            # always include llm for multi-agent explanation
            if "llm" in self.agents:
                agents.insert(0, self.agents["llm"])
        return [a for a in agents if a]
