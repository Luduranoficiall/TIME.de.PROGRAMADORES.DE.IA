from models import Tenant
from storage import SessionLocal
from auth import generate_token

def register_tenant(tenant_id: str, plan: str = "free"):
    db = SessionLocal()
    tenant = Tenant(id=tenant_id, plan=plan)
    db.add(tenant)
    db.commit()
    db.close()
    return {"tenant_id": tenant_id, "plan": plan, "token": generate_token(tenant_id)}

def activate_tenant(tenant_id: str):
    db = SessionLocal()
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if tenant:
        tenant.plan = "pro"
        db.commit()
    db.close()
    return {"tenant_id": tenant_id, "status": "activated"}

def welcome(tenant_id: str):
    return f"Bem-vindo, {tenant_id}! Sua conta está pronta para uso."
