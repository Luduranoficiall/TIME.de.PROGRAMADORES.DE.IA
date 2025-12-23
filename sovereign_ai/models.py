
from sqlalchemy import Column, String, Integer, Text, DateTime, Float
from sqlalchemy.sql import func
from storage import Base
from crypto_utils import encrypt, decrypt

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
    _output = Column("output", Text)
    score = Column(Integer)
    cost = Column(Float)
    created_at = Column(DateTime, server_default=func.now())

    @property
    def output(self):
        return decrypt(self._output) if self._output else None

    @output.setter
    def output(self, value):
        self._output = encrypt(value) if value else None

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(String, primary_key=True)
    tenant_id = Column(String)
    action = Column(String)
    detail = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
