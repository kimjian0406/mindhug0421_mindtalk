from app.models.emotion import Emotion
from app.models.user import User
from app.schemas.emotion import EmotionCreate
from tortoise.exceptions import DoesNotExist

async def create_emotion(user: User, emotion_data: EmotionCreate) -> Emotion:
    emotion = await Emotion.create(
        user=user,
        emotion=emotion_data.emotion,
        note=emotion_data.note
    )
    return emotion

async def get_emotions_by_user(user: User):
    return await Emotion.filter(user=user).order_by('-created_at')

