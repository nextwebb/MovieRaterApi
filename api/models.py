from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=360)
class Rating(models.Model):
    movie =models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MaxLengthValidator(1), MaxLengthValidator(5)])
    class Meta:
        unique_together = (('user', 'movie'))
        index_together = (('user', 'movie'))
