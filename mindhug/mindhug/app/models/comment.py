# app/models/comment.py
from tortoise import fields
from tortoise.models import Model

class Comment(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="comments")
    emotion_log = fields.ForeignKeyField("models.EmotionLog", related_name="comments")
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "comments"

