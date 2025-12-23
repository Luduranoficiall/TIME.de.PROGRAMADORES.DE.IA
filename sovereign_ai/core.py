from agents import AGENTS
from meta import plan, score, refine
from memory import Memory
from redis_cache import rate_limit
from vectors import embed, store_vector
from storage import SessionLocal
from models import Execution
from costs import calc_cost
from uuid import uuid4

class SovereignCore:
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id
        self.memory = Memory()

    def execute(self, intent: str):
        if not rate_limit(self.tenant_id, 100, 3600):
            return {"error": "RATE_LIMIT"}

        pipeline = plan(intent)
        output = intent
        iterations = 0

        for _ in range(5):
            for step in pipeline:
                agent = AGENTS.get(step)
                if agent:
                    output = agent.run(output)
                    self.memory.remember(output)

            s = score(output)
            iterations += 1
            if s >= 9:
                self.memory.store_truth(output, s)
                store_vector(self.tenant_id, output, embed(output))
                break
            output = refine(output)

        cost = calc_cost(iterations, len(output))
        db = SessionLocal()
        exec_id = str(uuid4())
        db.add(Execution(
            id=exec_id,
            tenant_id=self.tenant_id,
            intent=intent,
            output=output,
            score=s,
            cost=cost
        ))
        db.commit()
        db.close()

        return {
            "execution_id": exec_id,
            "output": output,
            "score": s,
            "cost": cost,
            "pipeline": pipeline
        }
