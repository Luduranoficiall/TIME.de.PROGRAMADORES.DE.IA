
from llm import llm

class Agent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def run(self, task: str) -> str:
        return llm(f"You are {self.name}, acting as {self.role}. Task:\n{task}")

ARCHITECT = Agent("Architect", "Senior Software Architect")
BACKEND = Agent("Backend", "Senior Backend Engineer")
REVIEWER = Agent("Reviewer", "Code Auditor")
SECURITY = Agent("Security", "Security Specialist")

AGENTS = {
    "Architect": ARCHITECT,
    "Backend": BACKEND,
    "Reviewer": REVIEWER,
    "Security": SECURITY,
}
