from app.agents.base import BaseAgent

class ReviewerAgent(BaseAgent):
    name = "Reviewer"
    role = "Code Auditor and Security Specialist"

    def review(self, code: str) -> str:
        return self.run(f"Review and improve this code:\n{code}")
