from fastapi import Depends, HTTPException, status
from app.services.auth import verify_access_token

def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_access_token(token)

