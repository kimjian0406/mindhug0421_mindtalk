# app/schemas/comment.py
from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    emotion_log_id: int
    content: str

class CommentOut(BaseModel):
    id: int
    emotion_log_id: int
    content: str
    created_at: datetime

    class Config:
        orm_mode = True

