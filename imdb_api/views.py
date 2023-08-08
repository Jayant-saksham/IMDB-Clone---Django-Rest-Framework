from django.http import HttpResponse, JsonResponse
from django.http import Http404

from .models import WatchList, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from .permissions import AdminOrReadOnly, ReviewUserOrReadOnly

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.serializers import ValidationError
from rest_framework.permissions import (IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'watchlist': reverse('watch-list', request=request, format=format),
        'streamplatform': reverse('stream-platform', request=request, format=format)
    })

class ReviewCreate(generics.CreateAPIView):
	serializer_class = ReviewSerializer
	# permission_classes = [ReviewUserOrReadOnly]

	def get_queryset(self):
		return Review.objects.all()

	def perform_create(self, serializer):
		pk = self.kwargs['pk']
		movie = WatchList.objects.get(pk = pk)
		review_user = self.request.user
		review_queryset = Review.objects.filter(review_user = review_user, watchlist = movie)
		if review_queryset:
			raise ValidationError("Cant review multiple times")
		if movie.number_rating == 0:
			movie.av_rating = serializer.validated_data['rating']
		else:
			movie.av_rating = (movie.av_rating + serializer.validated_data['rating'])/2

		movie.number_rating +=1
		movie.save()
		serializer.save(watchlist = movie, review_user = review_user)

class ReviewListView(generics.ListAPIView):
	permission_classes = [IsAuthenticated]
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer

	def get_queryset(self):
		pk = self.kwargs['pk']
		return Review.objects.filter(watchlist = pk)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [ReviewUserOrReadOnly]
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer




class StreamPlatformViewSet(viewsets.ModelViewSet):
	"""
	    This viewset automatically provides `list`, `create`, `retrieve`,
	    `update` and `destroy` actions."""
	queryset = StreamPlatform.objects.all()
	serializer_class = StreamPlatformSerializer


# class StreamPlatformList(generics.ListCreateAPIView):
# 	queryset = StreamPlatform.objects.all()
# 	serializer_class = StreamPlatformSerializer
#
# class StreamPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = StreamPlatform.objects.all()
# 	serializer_class = StreamPlatformSerializer



# class StreamPlatformList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#
# 	queryset = StreamPlatform.objects.all()
# 	serializer_class = StreamPlatformSerializer
#
# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)
#
# 	def post(self, request, *args, **kwargs):
# 		return self.create(request, *args, **kwargs)
#
# class StreamPlatformDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
# 	queryset = StreamPlatform.objects.all()
# 	serializer_class = StreamPlatformSerializer
#
# 	def get(self, request, *args, **kwargs):
# 		return self.retrieve(request, *args, **kwargs)
#
# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)
#
# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)




# class StreamPlatformList(APIView):
# 	"""
# 	    List all snippets, or create a new streamplatform.
# 	    """
# 	def get(self, request, format=None):
# 		stream_list = StreamPlatform.objects.all()
# 		serialized = StreamPlatformSerializer(stream_list, many = True)
# 		return Response(serialized.data)
#
# 	def post(self, request, format=None):
# 		_data = request.data
# 		serialized = StreamPlatformSerializer(data = _data)
# 		if serialized.is_valid():
# 			serialized.save()
# 			return Response(serialized.data, status = status.HTTP_201_CREATED)
# 		return Response(serialized.errors, status = status.HTTP_400_BAD_REQUEST)
#
# class StreamPlatformDetail(APIView):
# 	"""
# 	    Retrieve, update or delete a streamplatform instance.
# 	"""
# 	def get_object(self, pk):
# 		try:
# 			return StreamPlatform.objects.get(pk=pk)
# 		except StreamPlatform.DoesNotExist:
# 			raise Http404
# 	def get(self, request,pk, format=None):
# 		stream_platform = self.get_object(pk)
# 		serializer = StreamPlatformSerializer(stream_platform)
# 		return Response(serializer.data)
#
#
# 	def put(self, request,pk, format=None):
# 		stream_platform = self.get_object(pk)
# 		_data = request.data
# 		serializer = StreamPlatformSerializer(stream_platform, data = _data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# 	def delete(self,request, pk, format=None):
# 		stream_platform = self.get_object(pk)
# 		stream_platform.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def movie_list(request):
	movie_list = WatchList.objects.all()
	serialized = WatchListSerializer(movie_list, many = True)
	return Response(serialized.data)
@api_view(['GET'])
def movie_detail(request, pk):
	movie = WatchList.objects.get(pk = pk)
	serialized = WatchListSerializer(movie)
	return Response(serialized.data)
# # Particular = get, put, delte )pk
# # list = get, post pkno
#
# @api_view(['GET', 'POST'])
# def stream_list(request, format = None):
# 	"""
# 	    List all code streamplatform, or create a new streamplatform.
# 	"""
# 	if request.method == 'GET':
# 		stream_list = StreamPlatform.objects.all()
# 		serialized = StreamPlatformSerializer(stream_list, many = True)
# 		return Response(serialized.data)
#
# 	elif request.method == 'POST':
# 		_data = request.data
# 		serialized = StreamPlatformSerializer(data = _data)
# 		if serialized.is_valid():
# 			serialized.save()
# 			return Response(serialized.data, status = status.HTTP_201_CREATED)
# 		return Response(serialized.errors, status = status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def stream_detail(request, pk, format = None):
# 	"""
# 	    Retrieve, update or delete.
# 	"""
# 	try:
# 		stream_platform = StreamPlatform.objects.get(pk = pk)
# 	except StreamPlatform.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
#
# 	if request.method == 'GET':
# 		serializer = StreamPlatformSerializer(stream_platform)
# 		return Response(serializer.data)
#
# 	elif request.method == 'PUT':
# 		_data = request.data
# 		serializer = StreamPlatformSerializer(stream_platform, data = _data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# 	elif request.method == 'DELETE':
# 		stream_platform.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
#
