from .models import Movies
from .serializers import MoviesSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

class MoviesViewSet(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    
@api_view(['GET'])
def get_movies(request):
    queryset = Movies.objects.all()
    serializer = MoviesSerializer(queryset, many=True)
    return Response(serializer.data)