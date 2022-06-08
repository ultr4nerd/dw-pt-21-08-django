"""Movies app views"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer


@api_view(['GET', 'POST'])
def list_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(instance=movies, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        print(request.data)
        return Response({"message": "created"}, status=status.HTTP_201_CREATED)
