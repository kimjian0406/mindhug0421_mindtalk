from tortoise import fields
from tortoise.models import Model

class Movie(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    release_date = fields.DateField()
    
    class Meta:
        table = "movies"

