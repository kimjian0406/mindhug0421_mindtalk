from tortoise import fields
from tortoise.models import Model

class Movie(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200)
    description = fields.TextField()
    release_date = fields.DatetimeField()
    rating = fields.FloatField()

    def __str__(self):
        return self.title

