from fastapi import Header
from app.core.tenant import current_tenant

def get_tenant(x_tenant_id: str = Header(...)):
    current_tenant.set(x_tenant_id)
    return x_tenant_id
