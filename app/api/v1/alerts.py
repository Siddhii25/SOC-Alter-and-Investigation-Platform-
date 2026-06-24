from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from app.dependencies.auth import get_current_user #verify jwt token and check user is logged in or not 
from app.models.user import User 
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.alert import ( # for validationn 
    AlertCreate,
    AlertResponse,
    AlertUpdate
)

from app.services.alert_service import (    # logic 
    create_alert,
    get_all_alerts,
    get_alert_by_id,
    update_alert,
    delete_alert
)


router = APIRouter(  
    prefix="/alerts",
    tags=["Alerts"]
)


# POST : CREATE A ALERT (alert -> router -> database insert )
@router.post(
    "",
    response_model=AlertResponse
)
def create_new_alert(
    alert: AlertCreate, #Fastapi automatically validates incoming json 
    db: Session = Depends(get_db), # setting up database 
    current_user: User = Depends(get_current_user) # check jwt token -> confirm user -> give access 
):
    return create_alert(
        alert,
        db,
        current_user
    )

# RETRIEVE 
@router.get(
    "",
    response_model=list[AlertResponse]
)
def get_alerts(
    db: Session = Depends(get_db) # database connect 
): 
    return get_all_alerts(db)

# By id 
@router.get(
    "/{alert_id}",
    response_model=AlertResponse
)
def get_alert( 
    alert_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return get_alert_by_id(
            alert_id,
            db
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

# UPDATE 
@router.put(
    "/{alert_id}",
    response_model=AlertResponse
)
def update_existing_alert(
    alert_id: int,
    alert: AlertUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return update_alert(
            alert_id,
            alert,
            db
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

#delete 
@router.delete("/{alert_id}")
def delete_existing_alert(
    alert_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return delete_alert(
            alert_id,
            db
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )