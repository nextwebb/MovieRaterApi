from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .models import Movie, Rating, Comment
from .serializers import MovieSerializers, RatingSerializers, UserSerializers, CommentSerializers
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            print('user', user)
            # user = User.objects.get(id=1)

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializers(rating, many=False)
                response = {'message': 'Rating  Updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializers(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def comment_on_movie(self, request, pk=None):
        if 'message' in request.data:
            movie = Movie.objects.get(id=pk)
            message = request.data['message']
            user = request.user

            try:
                comment = Comment.objects.get(user=user.id, movie=movie.id)
                comment.message = message
                comment.save()
                serializer = CommentSerializers(comment, many=False)
                response = {'message': 'Comment  Updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            except Comment.DoesNotExist:
                comment = Comment.objects.create(user=user, movie=movie, message=message)
                serializer = CommentSerializers(comment, many=False)
                response = {'message': 'Comment created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide Comment'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], permission_classes=[IsAuthenticated] )
    def delete_comment(self, request, pk=None):
            movie = Movie.objects.get(id=pk)
            try :
                comment = Comment.objects.get(user=request.user.id, movie=movie.id)
                print(comment)
                comment.delete()
                response = {'message': 'Comment  Deleted!'}
                return Response(response, status=status.HTTP_200_OK)
            except :
                response = {'message': 'Cannot delete comment'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
    authentication_classes = (TokenAuthentication,)

    # prevent builtin default methods
    # using the model viewset it will be open the 5 methods
    # create, update, Retrieve, delete, list
    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update ratings like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create ratings like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    authentication_classes = (TokenAuthentication,)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update comments like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create comments like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
