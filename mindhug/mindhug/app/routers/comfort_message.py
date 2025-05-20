from fastapi import APIRouter, Depends, HTTPException
from app.schemas.comfort_message import ComfortMessageCreate, ComfortMessageRead
from app.models.comfort_message import ComfortMessage
from app.models.user import User
from app.utils.auth import get_current_user

router = APIRouter(prefix="/comfort-messages", tags=["Comfort Messages"])

@router.post("/", response_model=ComfortMessageRead)
async def create_comfort_message(
    message: ComfortMessageCreate,
    current_user: User = Depends(get_current_user)
):
    new_message = await ComfortMessage.create(content=message.content, user=current_user)
    return await ComfortMessageRead.from_tortoise_orm(new_message)

@router.get("/", response_model=list[ComfortMessageRead])
async def get_comfort_messages():
    return await ComfortMessageRead.from_queryset(ComfortMessage.all().order_by("-created_at"))

