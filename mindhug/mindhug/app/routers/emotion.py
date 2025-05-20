from fastapi import APIRouter
from app.models.emotion import Emotion
from app.schemas.emotion import EmotionCreate, EmotionResponse

router = APIRouter(prefix="/emotions", tags=["Emotions"])

@router.post("/", response_model=EmotionResponse)
async def create_emotion(emotion: EmotionCreate):
    obj = await Emotion.create(**emotion.dict())
    return await EmotionResponse.from_tortoise_orm(obj)

