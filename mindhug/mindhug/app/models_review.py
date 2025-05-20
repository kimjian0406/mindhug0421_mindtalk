from tortoise import fields
from tortoise.models import Model
from app.models.user import User  # User 모델을 참조
from app.models.movie import Movie  # Movie 모델을 참조

class Review(Model):
    id = fields.IntField(pk=True)
    movie = fields.ForeignKeyField("models.Movie", related_name="reviews")
    user = fields.ForeignKeyField("models.User", related_name="reviews")
    content = fields.TextField()
    rating = fields.IntField()  # 1~5점까지 리뷰 점수
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"Review for {self.movie.title} by {self.user.username}"

