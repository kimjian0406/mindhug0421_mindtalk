from tortoise import fields
from tortoise.models import Model

class ComfortMessage(Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    user = fields.ForeignKeyField("models.User", related_name="comfort_messages")

