from fastapi import FastAPI, Depends, Header
from pydantic import BaseModel
from core import SovereignCore
from auth import verify_token
from policies import allowed
from governance import audit

app = FastAPI(title="SOVEREIGN_AI_SYSTEM")

class Request(BaseModel):
    intent: str

@app.post("/execute")
def execute(
    req: Request,
    authorization: str = Header(...)
):
    payload = verify_token(authorization)
    tenant = payload["tenant"]

    if not allowed(req.intent):
        audit(tenant, "BLOCKED", req.intent)
        return {"error": "POLICY_BLOCK"}

    core = SovereignCore(tenant)
    result = core.execute(req.intent)
    audit(tenant, "EXECUTE", req.intent)
    return result

@app.get("/health")
def health():
    return {"status": "PRODUCTION_READY"}
