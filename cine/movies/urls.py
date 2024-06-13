from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import get_movies,create_showtime,success_view

router = DefaultRouter()
urlpatterns = [
    path('', get_movies, name="get_movies"),
    path('showtime', create_showtime, name="create_showtime"),
    path('showtime', success_view, name="success_url")
]


