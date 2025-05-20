from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)  # 기본키
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    hashed_password = fields.CharField(max_length=255)  # 비밀번호는 해시값으로 저장
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.username

