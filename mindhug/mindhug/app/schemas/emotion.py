from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EmotionCreate(BaseModel):
    user_id: int
    mood: str
    note: Optional[str] = None

class EmotionResponse(BaseModel):
    id: int
    user_id: int
    mood: str
    note: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

