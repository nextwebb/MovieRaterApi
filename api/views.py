from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Movie, Rating
from .serializers import MovieSerializers, RatingSerializers

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = (MovieSerializers)
    
    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        response = {'message': 'its working'}
        return Response(response, status=status.HTTP_200_OK)
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = (RatingSerializers)