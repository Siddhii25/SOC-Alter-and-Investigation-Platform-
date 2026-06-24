from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.dependencies.auth import get_current_user
from app.models.user import User
from app.services.auth_service import create_user
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.db.database import get_db

from app.dependencies.auth import get_current_user
from app.models.user import User

from app.schemas.user import (
    UserCreate,
    UserResponse
)
from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)

from app.services.auth_service import (
    create_user,
    login_user
)
 
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register_user(
    user: UserCreate, #incoming json validate 
    db: Session = Depends(get_db)
):
    try:
        return create_user(
            user,
            db
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    try:
        return login_user(
            form_data.username,
            form_data.password,
            db
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
    
@router.get("/me")
def get_me(
    current_user: User = Depends(
        get_current_user
    )
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }
