from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.models.user import User

from app.schemas.alert import (
    AlertCreate,
    AlertUpdate
)

from app.services.audit_log_service import (
    create_audit_log
)


def create_alert(
    alert_data: AlertCreate,
    db: Session,
    current_user: User
):
    alert = Alert(
        title=alert_data.title,
        description=alert_data.description,
        severity=alert_data.severity,
        source=alert_data.source
    )

    db.add(alert)
    db.commit()
    db.refresh(alert)

    create_audit_log(
        action="CREATE",
        entity_type="ALERT",
        entity_id=alert.id,
        performed_by=current_user.email,
        db=db
    )

    return alert


def get_all_alerts(
    db: Session
):
    return db.query(Alert).all()


def get_alert_by_id(
    alert_id: int,
    db: Session
):
    alert = (
        db.query(Alert)
        .filter(Alert.id == alert_id)
        .first()
    )

    if not alert:
        raise ValueError("Alert not found")

    return alert


def update_alert(
    alert_id: int,
    alert_data: AlertUpdate,
    db: Session
):
    alert = (
        db.query(Alert)
        .filter(Alert.id == alert_id)
        .first()
    )

    if not alert:
        raise ValueError("Alert not found")

    update_data = alert_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(alert, key, value)

    db.commit()
    db.refresh(alert)

    create_audit_log(
        action="UPDATE",
        entity_type="ALERT",
        entity_id=alert.id,
        performed_by="system",
        db=db
    )

    return alert


def delete_alert(
    alert_id: int,
    db: Session
):
    alert = (
        db.query(Alert)
        .filter(Alert.id == alert_id)
        .first()
    )

    if not alert:
        raise ValueError("Alert not found")

    db.delete(alert)
    db.commit()

    return {
        "message": "Alert deleted successfully"
    }