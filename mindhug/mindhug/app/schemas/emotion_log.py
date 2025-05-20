from pydantic import BaseModel
from datetime import datetime
from pydantic import BaseModel
from datetime import datetime

class EmotionLogCreate(BaseModel):
    user_id: int
    emotion: str
    content: str | None = None

class EmotionLogResponse(BaseModel):
    id: int
    user_id: int
    emotion: str
    content: str | None = None
    created_at: datetime

    class Config:
        orm_mode = True

class EmotionLogCreate(BaseModel):
    emotion: str
    content: str

class EmotionLogOut(BaseModel):
    id: int
    emotion: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True

