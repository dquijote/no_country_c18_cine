from .models import Movies, Showtimes
from .serializers import MoviesSerializer,ShowtimesSerializer
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ShowtimesSerializer

class MoviesViewSet(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    
@api_view(['GET'])
def get_movies(request):
    queryset = Movies.objects.all()
    serializer = MoviesSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_showtime(request):
    if request.method == 'POST':
        serializer = ShowtimesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        queryset = Showtimes.objects.all()
        serializer = ShowtimesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
def success_view(request):
    return Response({"message": "Showtime created successfully"}, status=status.HTTP_200_OK)   