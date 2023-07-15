from django.urls import path, include
from . import views
urlpatterns = [
    path('movies/', views.WatchListView.as_view(), name="watchlist"),
    path('movies/<int:pk>', views.WatchListDetailView.as_view(), name="watchlist-detail"),
]
