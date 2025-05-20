from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import create_user, get_user_by_email
from app.models.user import User
from app.db import get_session  # 나중에 db.py 만들 거야

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserRead)
def register(user_create: UserCreate, session: Session = Depends(get_session)):
    existing_user = get_user_by_email(session, user_create.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(session, user_create)

