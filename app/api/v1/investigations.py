from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.investigation import (
    InvestigationCreate,
    InvestigationResponse,
    InvestigationUpdate
)

from app.services.investigation_service import (
    create_investigation,
    get_all_investigations,
    get_investigation_by_id,
    update_investigation
)

from app.dependencies.auth import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/investigations",
    tags=["Investigations"]
)


@router.post(
    "",
    response_model=InvestigationResponse
)
def create_new_investigation(
    investigation: InvestigationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_investigation(
        investigation,
        db
    )


@router.get(
    "",
    response_model=list[InvestigationResponse]
)
def get_investigations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_investigations(db)


@router.get(
    "/{investigation_id}",
    response_model=InvestigationResponse
)
def get_investigation(
    investigation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return get_investigation_by_id(
            investigation_id,
            db
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.put(
    "/{investigation_id}",
    response_model=InvestigationResponse
)
def update_existing_investigation(
    investigation_id: int,
    investigation: InvestigationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return update_investigation(
            investigation_id,
            investigation,
            db
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )