from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)

from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"

