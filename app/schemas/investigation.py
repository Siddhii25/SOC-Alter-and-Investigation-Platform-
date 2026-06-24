from pydantic import BaseModel


class InvestigationCreate(BaseModel):
    alert_id: int
    assigned_to_user_id: int
    findings: str
    evidence: str
    risk_level: str
    containment_action: str


class InvestigationUpdate(BaseModel):
    findings: str | None = None
    evidence: str | None = None
    risk_level: str | None = None
    containment_action: str | None = None
    resolution: str | None = None
    status: str | None = None


class InvestigationResponse(BaseModel):
    id: int
    alert_id: int
    assigned_to_user_id: int
    findings: str | None = None
    evidence: str | None = None
    risk_level: str | None = None
    containment_action: str | None = None
    resolution: str | None = None
    status: str

    class Config:
        from_attributes = True