from pydantic import BaseModel
from datetime import datetime

class ComfortMessageCreate(BaseModel):
    content: str

class ComfortMessageRead(BaseModel):
    id: int
    content: str
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True

