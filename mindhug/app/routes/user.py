from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test_user_router():
    return {"message": "user router 연결 성공!"}
from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserOut
from app.models.user import User
from app.services.auth import hash_password

router = APIRouter()

@router.post("/signup", response_model=UserOut)
async def signup(user: UserCreate):
    existing_user = await User.get_or_none(email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw = hash_password(user.password)
    new_user = await User.create(
        email=user.email,
        username=user.username,
        password=hashed_pw
    )
    return new_user

from fastapi import APIRouter, HTTPException, Depends
from tortoise.exceptions import DoesNotExist
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.models.user import User
from passlib.context import CryptContext
from datetime import datetime

router = APIRouter(prefix="/users", tags=["Users"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


@router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate):
    existing_user = await User.filter(email=user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = await User.create(
        email=user_data.email,
        username=user_data.username,
        password=hash_password(user_data.password),
        created_at=datetime.utcnow(),
    )
    return user


@router.post("/login")
async def login(user_data: UserLogin):
    user = await User.filter(email=user_data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not pwd_context.verify(user_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"message": f"Welcome back, {user.username}!"}

