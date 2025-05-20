from tortoise import fields
from tortoise.models import Model

class Review(Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    movie_id = fields.IntField()
    user_id = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "reviews"

