from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func #func.now()-> for timestamp 

from app.db.session import Base


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(Text)

    severity = Column(String, nullable=False)

    status = Column(String, default="NEW")

    source = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
