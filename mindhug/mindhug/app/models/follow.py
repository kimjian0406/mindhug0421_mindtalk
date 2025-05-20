# app/models/follow.py

from tortoise import fields
from tortoise.models import Model

class Follow(Model):
    id = fields.IntField(pk=True)
    follower = fields.ForeignKeyField("models.User", related_name="following")
    following = fields.ForeignKeyField("models.User", related_name="followers")
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "following")

