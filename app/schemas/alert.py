from pydantic import BaseModel

class AlertCreate(BaseModel):
    title: str
    description: str
    severity: str
    source: str


class AlertResponse(BaseModel):
    id: int
    title: str
    description: str
    severity: str
    status: str
    source: str

    class Config:
        from_attributes = True

class AlertUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    severity: str | None = None
    status: str | None = None
    source: str | None = None