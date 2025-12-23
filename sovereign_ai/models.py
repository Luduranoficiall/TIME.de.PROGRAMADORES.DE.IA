from sqlalchemy import Column, String, Integer, Text, DateTime, Float
from sqlalchemy.sql import func
from storage import Base

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(String, primary_key=True)
    plan = Column(String, default="free")
    created_at = Column(DateTime, server_default=func.now())

class Execution(Base):
    __tablename__ = "executions"
    id = Column(String, primary_key=True)
    tenant_id = Column(String, index=True)
    intent = Column(Text)
    output = Column(Text)
    score = Column(Integer)
    cost = Column(Float)
    created_at = Column(DateTime, server_default=func.now())

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(String, primary_key=True)
    tenant_id = Column(String)
    action = Column(String)
    detail = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
