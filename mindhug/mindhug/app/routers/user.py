from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.schemas.user import UserCreate, UserRead
from app.utils.auth import hash_password

router = APIRouter()

@router.post("/register", response_model=UserRead)
async def register(user: UserCreate):
    existing = await User.get_or_none(username=user.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_pw = hash_password(user.password)
    new_user = await User.create(username=user.username, password=hashed_pw)
    return new_user

