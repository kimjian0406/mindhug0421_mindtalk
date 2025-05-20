from fastapi import Depends, HTTPException
from pydantic import BaseModel
from app.models.user import User
from app.services.auth import create_access_token

class UserLogin(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login(user_login: UserLogin):
    user = await User.verify_password(user_login.email, user_login.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

