from fastapi import APIRouter, Depends
from app.api.deps import get_tenant
from app.agents.orchestrator import Orchestrator
from pydantic import BaseModel

router = APIRouter(prefix="/v1")
orchestrator = Orchestrator()

class RunRequest(BaseModel):
    requirement: str

@router.post("/execute")
def execute(req: RunRequest, tenant=Depends(get_tenant)):
    return orchestrator.execute(req.requirement)


# ----------------- GOD MODE API -----------------
from app.agents.orchestrator import GodModeOrchestrator

router_v3 = APIRouter(prefix="/v3")

class GodRequest(BaseModel):
    intent: str
    root_key: str

@router_v3.post("/god/execute")
def god_execute(req: GodRequest):
    orchestrator = GodModeOrchestrator(req.root_key)
    return orchestrator.execute(req.intent)
