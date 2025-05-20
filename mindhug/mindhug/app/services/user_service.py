from sqlmodel import Session, select
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

def create_user(session: Session, user_create: UserCreate) -> User:
    user = User(
        email=user_create.email,
        username=user_create.username,
        hashed_password=get_password_hash(user_create.password)
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_user_by_email(session: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()

