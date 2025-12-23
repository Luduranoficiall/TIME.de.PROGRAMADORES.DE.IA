from app.agents.base import BaseAgent

class ArchitectAgent(BaseAgent):
    name = "Architect"
    role = "Senior Software Architect"

    def design(self, requirements: str) -> str:
        return self.run(f"Design system architecture for: {requirements}")
