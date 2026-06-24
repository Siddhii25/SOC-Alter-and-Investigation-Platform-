from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.audit_log import (
    AuditLogResponse
)

from app.services.audit_log_service import (
    get_all_audit_logs
)

from app.dependencies.auth import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/audit-logs",
    tags=["Audit Logs"]
)


@router.get(
    "",
    response_model=list[AuditLogResponse]
)
def get_logs(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    return get_all_audit_logs(db)