AUDIT_LOG = []

def audit(tenant, action, detail):
    AUDIT_LOG.append({
        "tenant": tenant,
        "action": action,
        "detail": detail
    })
