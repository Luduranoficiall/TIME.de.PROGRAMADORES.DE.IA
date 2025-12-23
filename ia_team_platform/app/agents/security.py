from app.agents.base import BaseAgent

class SecurityAgent(BaseAgent):
    name = "Security Auditor"
    role = "Application Security Specialist"

    def run(self, code: str) -> str:
        return super().run(
            f"Audit this code for security vulnerabilities:\n{code}"
        )
