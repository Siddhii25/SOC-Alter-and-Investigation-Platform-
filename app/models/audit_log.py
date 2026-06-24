from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.db.session import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    action = Column(String, nullable=False)

    entity_type = Column(String, nullable=False)

    entity_id = Column(Integer)

    performed_by = Column(String)

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )