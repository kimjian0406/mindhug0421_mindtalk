from fastapi import FastAPI
from app.routes import emotion_diary
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

app.include_router(emotion_diary.router)

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models.emotion_diary", "app.models.user"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models.user", "app.models.emotion_diary"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Mindhug 서버에 오신 걸 환영합니다!"}

from fastapi import FastAPI
from app.routes import user

app = FastAPI()

app.include_router(user.router)

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models.user"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
async def root():
    return {"message": "Hello, mindhug"}

from app.routes import user
app.include_router(user.router)

from fastapi import FastAPI
from app.routes import user
app = FastAPI()

app.include_router(user.router)
from app.routes.user import router as user_router

app.include_router(user_router, prefix="/users")

from fastapi import FastAPI
from app.routes import user  # 또는: from app.routes.user import router as user_router

app = FastAPI()

app.include_router(user.router, prefix="/users")  # 또는: app.include_router(user_router, prefix="/users")

from fastapi import FastAPI
from app.routes import user
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

app.include_router(user.router, prefix="/users")

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models.user"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

from fastapi import FastAPI
from app.routes import user

app = FastAPI()

app.include_router(user.router)
