from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.models.user import User
from app.models.movie import Movie
from app.models.review import Review
from fastapi import FastAPI
from app.routers import user
from app.routers import follow
from fastapi import FastAPI
from app.db import init_db
from app.routers import emotion_log
from app.routers import comfort_message
from app.routers import user, emotion_log
# ...
app.include_router(user.router)

app.include_router(comfort_message.router)

app = FastAPI()
init_db(app)

app.include_router(emotion_log.router)

@app.get("/")
async def root():
    return {"message": "Hello, mindhug!"}


app.include_router(follow.router)

app = FastAPI()

app.include_router(user.router)

app = FastAPI()

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",  # 로컬 SQLite DB 사용
    modules={"models": ["app.models.user", "app.models.movie", "app.models.review"]},
    generate_schemas=True,  # 앱 실행 시 자동으로 DB 스키마 생성
    add_exception_handlers=True,
)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

modules={"models": [
    "app.models.user", "app.models.movie", "app.models.review",
    "app.models.emotion_log", "app.models.comment", "app.models.follow"
]}

