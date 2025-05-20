from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

# 데이터베이스 설정
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",  # SQLite 사용 (추후 변경 가능)
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Mindhug!"}

