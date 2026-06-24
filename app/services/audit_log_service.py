from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog


def create_audit_log(
    action: str,
    entity_type: str,
    entity_id: int,
    performed_by: str,
    db: Session
):
    log = AuditLog(
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        performed_by=performed_by
    )

    db.add(log)
    db.commit()

    return log


def get_all_audit_logs(
    db: Session
):
    return db.query(AuditLog).all()