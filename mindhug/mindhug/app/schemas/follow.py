# app/schemas/follow.py

from pydantic import BaseModel

class FollowCreate(BaseModel):
    following_id: int

