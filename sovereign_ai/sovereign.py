from agents import ARCHITECT, BACKEND, REVIEWER, SECURITY
from meta import plan, score, refine
from memory import Memory
from config import ROOT_KEY, MAX_ITERATIONS, MIN_SCORE

AGENTS = {
    "Architect": ARCHITECT,
    "Backend": BACKEND,
    "Reviewer": REVIEWER,
    "Security": SECURITY,
}

class SovereignAI:
    def __init__(self, root_key: str):
        if root_key != ROOT_KEY:
            raise PermissionError("UNAUTHORIZED")

        self.memory = Memory()

    def execute(self, intent: str) -> dict:
        pipeline = plan(intent)
        output = intent
        iterations = 0

        for _ in range(MAX_ITERATIONS):
            for step in pipeline:
                agent = AGENTS.get(step)
                if agent:
                    output = agent.run(output)
                    self.memory.remember(output)

            s = score(output)
            iterations += 1

            if s >= MIN_SCORE:
                self.memory.store_truth(output, s)
                break

            output = refine(output)

        return {
            "output": output,
            "score": s,
            "iterations": iterations,
            "pipeline": pipeline,
            "memory_truth": self.memory.recall_truth()
        }
