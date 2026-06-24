from fastapi import FastAPI
from app.db.session import Base
from app.db.database import engine
from app.api.v1.auth import router as auth_router
from app.models.user import User
from app.models.alert import Alert
from app.models.investigation import Investigation
from app.models.audit_log import AuditLog
from app.api.v1.alerts import router as alert_router
from app.core.config import settings
from app.api.v1.investigations import (
    router as investigation_router
)

from app.api.v1.audit_logs import (
    router as audit_log_router
)


app = FastAPI(
    title=settings.APP_NAME
)
app.include_router(auth_router)
app.include_router(alert_router)
app.include_router(
    investigation_router
)
app.include_router(
    audit_log_router
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "SOC Alert Investigation Platform"
    }