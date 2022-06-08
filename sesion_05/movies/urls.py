"""Movies app URL config"""

from django.urls import path

from .views import list_movies

app_name = "movies"
urlpatterns = [
    path("movies/", list_movies, name="list"),
]
