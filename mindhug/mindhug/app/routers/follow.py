# app/routers/follow.py

from fastapi import APIRouter, Depends, HTTPException
from app.schemas.follow import FollowCreate
from app.models.follow import Follow
from app.models.user import User
from app.utils.auth import get_current_user

router = APIRouter(prefix="/follows", tags=["Follow"])

@router.post("/")
async def follow_user(data: FollowCreate, current_user: User = Depends(get_current_user)):
    if current_user.id == data.following_id:
        raise HTTPException(status_code=400, detail="자기 자신은 팔로우할 수 없습니다.")
    
    exists = await Follow.filter(follower=current_user.id, following=data.following_id).exists()
    if exists:
        raise HTTPException(status_code=400, detail="이미 팔로우했습니다.")
    
    await Follow.create(follower=current_user, following_id=data.following_id)
    return {"message": "팔로우 성공"}

@router.delete("/{user_id}")
async def unfollow_user(user_id: int, current_user: User = Depends(get_current_user)):
    deleted_count = await Follow.filter(follower=current_user.id, following_id=user_id).delete()
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="팔로우 관계가 없습니다.")
    return {"message": "언팔로우 성공"}

@router.get("/following")
async def get_following(current_user: User = Depends(get_current_user)):
    return await User.filter(followers__follower=current_user).all()

@router.get("/followers")
async def get_followers(current_user: User = Depends(get_current_user)):
    return await User.filter(following__following=current_user).all()

