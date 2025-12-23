from app.infra.llm import generate

class AgentFactory:
    def create(self, specialty: str) -> dict:
        prompt = f"""
        Define a new AI agent with:
        - Name
        - Role
        - Responsibilities
        for specialty: {specialty}
        """
        return {"definition": generate(prompt)}
