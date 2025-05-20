from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.db import init_db
from app.routers import user, follow, emotion_log, comfort_message

app = FastAPI()

# DB 초기화 (init_db 함수가 있으면 호출)
init_db(app)

# 라우터 등록
app.include_router(user.router)
app.include_router(follow.router)
app.include_router(emotion_log.router)
app.include_router(comfort_message.router)

# Tortoise ORM 자동 등록
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={
        "models": [
            "app.models.user",
            "app.models.movie",
            "app.models.review",
            "app.models.emotion_log",
            "app.models.comment",
            "app.models.follow",
        ]
    },
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
async def root():
    return {"message": "Hello, mindhug!"}

