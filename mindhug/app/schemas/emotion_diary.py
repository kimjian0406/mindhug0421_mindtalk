from pydantic import BaseModel
from datetime import datetime

class EmotionDiaryCreate(BaseModel):
    emotion: str
    content: str

class EmotionDiaryOut(BaseModel):
    id: int
    emotion: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True

