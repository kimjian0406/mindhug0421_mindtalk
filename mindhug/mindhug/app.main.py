from fastapi import FastAPI
from app.routes import user
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# DB 연결 설정
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models.user"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

