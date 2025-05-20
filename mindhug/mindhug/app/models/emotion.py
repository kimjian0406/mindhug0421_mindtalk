from tortoise import fields
from tortoise.models import Model

class Emotion(Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    mood = fields.CharField(max_length=100)
    note = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "emotions"

