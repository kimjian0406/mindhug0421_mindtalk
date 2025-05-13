from fastapi import Depends, status
from app.schemas.user import UserLogin, Token
from app.services.jwt import create_access_token
from app.services.auth import verify_password

@router.post("/login", response_model=Token)
async def login(user_data: UserLogin):
    user = await User.get_or_none(email=user_data.email)
    if not user or not verify_password(user_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="이메일 또는 비밀번호가 틀렸습니다.")
    
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

