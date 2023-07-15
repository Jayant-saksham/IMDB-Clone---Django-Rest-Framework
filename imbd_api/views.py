from django.shortcuts import  HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . models import Review, WatchList, StreamPlatform
from .serializers import WatchListSerializer

class WatchListView(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serialized = WatchListSerializer(movies, many=True)
        return Response(serialized.data) 

    def post(self, request):
        data = request.data 
        serialized = WatchListSerializer(data = data) 
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status = 201)
        else:
            return Response(serialized.errors, status = 400) 
        

class WatchListDetailView(APIView):

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except:
            return Response({"Error": "Not Found"}, status = 404)
        
        serialized = WatchListSerializer(movie) 
        return Response(serialized.data)

    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except:
            return Response({"Error": "Not Found"}, status = 404)
        data = request.data 
        serialized = WatchListSerializer(movie, data = data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status = 201) 
        else:
            return Response(serialized.errors, status = 400)
        
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
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
        
        