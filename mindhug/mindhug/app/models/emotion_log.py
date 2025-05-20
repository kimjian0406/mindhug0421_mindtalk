# app/models/emotion_log.py
from tortoise import fields
from tortoise.models import Model
from tortoise import fields, models

class EmotionLog(models.Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    emotion = fields.CharField(max_length=50)
    content = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "emotion_logs"

class EmotionLog(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="emotion_logs")
    emotion = fields.CharField(max_length=20)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "emotion_logs"

