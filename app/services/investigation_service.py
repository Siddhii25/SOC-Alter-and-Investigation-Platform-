from sqlalchemy.orm import Session

from app.models.investigation import Investigation
from app.schemas.investigation import (
    InvestigationCreate,
    InvestigationUpdate
)
from app.services.audit_log_service import (
    create_audit_log
)

def create_investigation(
    investigation_data: InvestigationCreate,
    db: Session
):
    investigation = Investigation(
        alert_id=investigation_data.alert_id,
        assigned_to_user_id=investigation_data.assigned_to_user_id,
        findings=investigation_data.findings,
        evidence=investigation_data.evidence,
        risk_level=investigation_data.risk_level,
        containment_action=investigation_data.containment_action
    )

    db.add(investigation)
    db.commit()
    db.refresh(investigation)
    create_audit_log(
        action="CREATE",
        entity_type="INVESTIGATION",
        entity_id=investigation.id,
        performed_by="system",
        db=db
    )

    return investigation


def get_all_investigations(
    db: Session
):
    return db.query(Investigation).all()

def get_investigation_by_id(
    investigation_id: int,
    db: Session
):
    investigation = (
        db.query(Investigation)
        .filter(
            Investigation.id == investigation_id
        )
        .first()
    )

    if not investigation:
        raise ValueError(
            "Investigation not found"
        )

    return investigation

def update_investigation(
    investigation_id: int,
    investigation_data: InvestigationUpdate,
    db: Session
):
    investigation = (
        db.query(Investigation)
        .filter(
            Investigation.id == investigation_id
        )
        .first()
    )

    if not investigation:
        raise ValueError(
            "Investigation not found"
        )

    update_data = (
        investigation_data.model_dump(
            exclude_unset=True
        )
    )

    for key, value in update_data.items():
        setattr(
            investigation,
            key,
            value
        )

    db.commit()
    db.refresh(
        investigation
    )
    create_audit_log(
        action="UPDATE",
        entity_type="INVESTIGATION",
        entity_id=investigation.id,
        performed_by="system",
        db=db
    )

    return investigation