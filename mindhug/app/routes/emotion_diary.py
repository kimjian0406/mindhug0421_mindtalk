from fastapi import APIRouter, Depends
from app.models.emotion_diary import EmotionDiary
from app.schemas.emotion_diary import EmotionDiaryCreate, EmotionDiaryOut

# 임시 사용자 정보 (테스트용)
def get_current_user():
    return 1  # 임시로 user_id=1 사용

router = APIRouter(prefix="/emotion-diary", tags=["Emotion Diary"])

@router.post("/", response_model=EmotionDiaryOut)
async def create_emotion_diary(entry: EmotionDiaryCreate, user_id=Depends(get_current_user)):
    diary = await EmotionDiary.create(user_id=user_id, **entry.dict())
    return diary

@router.get("/", response_model=list[EmotionDiaryOut])
async def get_user_emotion_diaries(user_id=Depends(get_current_user)):
    return await EmotionDiary.filter(user_id=user_id).order_by("-created_at")

