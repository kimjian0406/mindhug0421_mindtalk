from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
from pydantic import BaseModel

class UserOut(BaseModel):
    username: str

    class Config:
        orm_mode = True

class UserRead(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

