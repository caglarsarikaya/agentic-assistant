"""Planner that routes tasks to other agents."""
from typing import Any, List


from app.agents.base import BaseAgent


class PeerAgent(BaseAgent):
    def __init__(self, short_memory, long_memory, agents: List[BaseAgent]):
        super().__init__("peer", "Planner and router", short_memory, long_memory)
        self.agents: List[BaseAgent] = agents


    def execute(self, session_id: str, task: str) -> Any:
        self.log(session_id, f"planner received: {task}")
        chosen_agents = self.plan(task)
        results = {}
        for agent in chosen_agents:
            results[agent.name] = agent.execute(session_id, task)
        self.log(session_id, f"planner results: {results}")
        return results

def plan(self, task: str) -> List[BaseAgent]:
        agents: List[BaseAgent] = [a for a in self.agents if a is not self and a.can_handle(task)]
        llm = next((a for a in self.agents if a.name == "llm"), None)
        if not agents:
            if llm:
                agents = [llm]
        else:
            if llm and llm not in agents:
                agents.insert(0, llm)
        return agents
