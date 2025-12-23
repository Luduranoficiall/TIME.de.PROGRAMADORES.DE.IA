from app.agents.base import BaseAgent

class BackendAgent(BaseAgent):
    name = "Backend Engineer"
    role = "Senior Backend Developer"

    def implement(self, spec: str) -> str:
        return self.run(f"Implement backend code for: {spec}")
