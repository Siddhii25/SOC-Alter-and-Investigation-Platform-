from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.db.session import Base


class Investigation(Base):
    __tablename__ = "investigations"

    id = Column(Integer, primary_key=True, index=True)

    alert_id = Column(
        Integer,
        ForeignKey("alerts.id")
    )

    assigned_to_user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    findings = Column(Text)

    evidence = Column(Text)

    risk_level = Column(String)

    containment_action = Column(Text)

    resolution = Column(Text)

    status = Column(String, default="OPEN")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )