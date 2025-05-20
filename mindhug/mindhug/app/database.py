from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

def init_db(app: FastAPI):
    register_tortoise(
        app,
        db_url="sqlite://db.sqlite3",
        modules={"models": ["app.models.emotion_log"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models.emotion_log", "app.models.user"]},
    ...
)

