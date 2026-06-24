from pydantic import BaseModel


class AuditLogResponse(BaseModel):
    id: int
    action: str
    entity_type: str
    entity_id: int | None = None
    performed_by: str | None = None

    class Config:
        from_attributes = True