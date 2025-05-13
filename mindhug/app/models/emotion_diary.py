from tortoise import fields, models

class EmotionDiary(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="emotion_diaries")
    emotion = fields.CharField(max_length=20)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "emotion_diary"

