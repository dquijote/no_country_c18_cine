from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import get_movies

router = DefaultRouter()
urlpatterns = [
    path('', get_movies, name="get_movies"),
]


