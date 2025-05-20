# app/routers/emotion_log.py
from fastapi import APIRouter, Depends
from tortoise.contrib.pydantic import pydantic_model_creator
from app.models.emotion_log import EmotionLog
from app.schemas.emotion_log import EmotionLogCreate, EmotionLogOut
from app.utils.auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/emotion-log", response_model=EmotionLogOut)
async def create_log(log: EmotionLogCreate, user: User = Depends(get_current_user)):
    obj = await EmotionLog.create(user=user, **log.dict())
    return await EmotionLogOut.from_tortoise_orm(obj)

@router.get("/emotion-log", response_model=list[EmotionLogOut])
async def get_logs(user: User = Depends(get_current_user)):
    logs = await EmotionLog.filter(user=user).order_by("-created_at")
    return logs

from fastapi import APIRouter
from app.schemas.emotion_log import EmotionLogCreate, EmotionLogResponse
from app.models.emotion_log import EmotionLog

router = APIRouter(prefix="/emotion", tags=["EmotionLog"])

@router.post("/", response_model=EmotionLogResponse)
async def create_emotion_log(log: EmotionLogCreate):
    emotion_log = await EmotionLog.create(**log.dict())
    return emotion_log

