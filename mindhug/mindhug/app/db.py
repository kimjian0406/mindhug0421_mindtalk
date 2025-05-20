from sqlmodel import create_engine, SQLModel, Session
from tortoise.contrib.fastapi import register_tortoise

DATABASE_URL = "sqlite:///./mindhug.db"  # SQLite DB 경로

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session  # 세션을 yield 해서 FastAPI 의존성 주입에 활용 가능

def init_db(app):
    register_tortoise(
        app,
        db_url="sqlite://db.sqlite3",  # Tortoise ORM용 DB URL
        modules={"models": ["app.models.emotion_log"]},  # 모델 모듈 경로
        generate_schemas=True,  # 앱 시작 시 자동 스키마 생성
        add_exception_handlers=True,
    )

