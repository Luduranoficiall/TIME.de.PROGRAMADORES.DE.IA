from contextvars import ContextVar

current_tenant: ContextVar[str] = ContextVar("current_tenant")
