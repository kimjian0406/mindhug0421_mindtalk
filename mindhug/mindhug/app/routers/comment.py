# app/routers/comment.py
from fastapi import APIRouter, Depends
from app.models.comment import Comment
from app.schemas.comment import CommentCreate, CommentOut
from app.utils.auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/comments", response_model=CommentOut)
async def create_comment(comment: CommentCreate, user: User = Depends(get_current_user)):
    obj = await Comment.create(user=user, emotion_log_id=comment.emotion_log_id, content=comment.content)
    return await CommentOut.from_tortoise_orm(obj)

@router.get("/comments/{emotion_log_id}", response_model=list[CommentOut])
async def get_comments(emotion_log_id: int):
    comments = await Comment.filter(emotion_log_id=emotion_log_id).order_by("-created_at")
    return comments

from app.utils.filter import contains_bad_word

@router.post("/comments", response_model=CommentOut)
async def create_comment(comment: CommentCreate, user: User = Depends(get_current_user)):
    if contains_bad_word(comment.content):
        return {"error": "부적절한 단어가 포함되어 있습니다."}
    
    obj = await Comment.create(user=user, emotion_log_id=comment.emotion_log_id, content=comment.content)
    return await CommentOut.from_tortoise_orm(obj)

