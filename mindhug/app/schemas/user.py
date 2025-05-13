from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Config:
        from_attributes = True  # Pydantic v2 기준

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# 회원가입 요청용 스키마
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


# 로그인 요청용 스키마
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# 응답용 스키마
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    created_at: datetime

    class Config:
        from_attributes = True  # orm_mode in Pydantic v1

