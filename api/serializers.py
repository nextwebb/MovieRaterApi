from rest_framework import serializers
from .models import Movie, Rating

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model: Movie
        fields: ('id','title', 'description',)

class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model: Rating
        fields: ('id','title', 'users',)