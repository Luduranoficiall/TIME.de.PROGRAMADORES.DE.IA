from abc import ABC
from app.infra.llm import generate
from app.memory.short_term import ShortTermMemory
from app.rag.retriever import retrieve_context

class BaseAgent(ABC):
    name: str
    role: str

    def __init__(self):
        self.memory = ShortTermMemory()

    def run(self, task: str) -> str:
        context = retrieve_context(task)
        prompt = f"""
        You are {self.name}, acting as {self.role}.

        Context:
        {context}

        Task:
        {task}
        """
        response = generate(prompt)
        self.memory.add(response)
        return response
