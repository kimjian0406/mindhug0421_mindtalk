from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

# 라우터 import
from app.routers import user, emotion_log, comment

app = FastAPI()

# DB 초기화
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models.user", "app.models.emotion_log"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

# 라우터 등록
app.include_router(user.router)
app.include_router(emotion_log.router)
app.include_router(comment.router)

@app.get("/")
async def root():
    return {"message": "Hello, mindhug!"}

