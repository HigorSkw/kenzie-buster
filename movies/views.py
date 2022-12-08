from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Movie
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer
from users.permissions import IsAdminOrReadOnly


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()

        seriliazer = MovieSerializer(movies, many=True)

        return Response(seriliazer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:

        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(owner=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    def get(self, request: Request, movie_id: int) -> Response:
        try:
            movie = Movie.objects.get(id=movie_id)
        except:
            return Response({"detail": "movie not found"}, status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
