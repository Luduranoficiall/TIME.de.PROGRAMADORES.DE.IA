from fastapi import FastAPI
from pydantic import BaseModel
from sovereign import SovereignAI

app = FastAPI(title="SOVEREIGN AI SYSTEM")

class Request(BaseModel):
    intent: str
    root_key: str

@app.post("/execute")
def execute(req: Request):
    ai = SovereignAI(req.root_key)
    return ai.execute(req.intent)

@app.get("/health")
def health():
    return {"status": "LEGENDARY"}
