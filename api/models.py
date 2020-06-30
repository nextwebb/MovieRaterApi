from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=360)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        # returns an array of rating object for a specific movie
        # self represent an instance of a class
        # so we're essentially checking if the ratings class, contains an instance of the movie object
        # the filter method returns the number of movie object in the array
        return len(ratings)

    def avg_rating(self):
        total = 0
        ratings = Rating.objects.filter(movie=self)
        # returns an array of rating object for a specific movie
        for rating in ratings:
            total += rating.stars
        if len(ratings) > 0:
            return total / len(ratings)
        else:
            return 0


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('user', 'movie')
        index_together = ('user', 'movie')
