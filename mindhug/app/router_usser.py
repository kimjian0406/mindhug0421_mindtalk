from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test():
    return {"message": "user router 연결 성공!"}

