from django.shortcuts import  HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . models import Movie
from .serializers import MovieSerializer

class MovieListView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serialized = MovieSerializer(movies, many=True)
        return Response(serialized.data) 

    def post(self, request):
        data = request.data 
        serialized = MovieSerializer(data = data) 
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status = 201)
        else:
            return Response(serialized.errors, status = 400) 
        

class MovieDetailView(APIView):

    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serialized = MovieSerializer(movie) 
        return Response(serialized.data)

    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        data = request.data 
        serialized = MovieSerializer(movie, data = data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status = 201) 
        else:
            return Response(serialized.errors, status = 400)
        
    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response({"Status": "Movie Deleted"}, status = 204)


# Create your views here.
# @api_view(['GET', 'POST'])
# def movies_list(request):

#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serialized = MovieSerializer(movies, many=True)
#         return Response(serialized.data)
    
#     elif request.method == 'POST':
#         data = request.data 
#         serialized = MovieSerializer(data = data) 
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status = 201)
        

# @api_view(['GET', 'PUT'])
# def movie_detail(request, pk):
    
#     movie = Movie.objects.get(pk=pk)
#     if request.method == 'GET':
#         serialized = MovieSerializer(movie) 
#         return Response(serialized.data)
    
#     elif request.method == 'PUT':
#         data = request.data 
#         serialized = MovieSerializer(movie, data = data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status = 201) 
        
        