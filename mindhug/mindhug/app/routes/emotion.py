from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.emotion import EmotionCreate, EmotionResponse
from app.services.emotion import create_emotion, get_emotions_by_user
from app.services.user import get_current_user
from app.models.user import User

router = APIRouter(prefix="/emotions", tags=["Emotions"])

@router.post("/", response_model=EmotionResponse)
async def create_emotion_record(
    emotion_data: EmotionCreate,
    current_user: User = Depends(get_current_user)
):
    return await create_emotion(current_user, emotion_data)

@router.get("/", response_model=List[EmotionResponse])
async def list_my_emotions(current_user: User = Depends(get_current_user)):
    return await get_emotions_by_user(current_user)

