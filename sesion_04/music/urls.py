"""Music app url config"""

from django.urls import path

from . import views


app_name = "music"
urlpatterns = [
    path("songs/", views.show_songs, name="show_songs"),
    path("create-artist/", views.create_artist, name="create_artist"),
    path("create-song/", views.create_song, name="create_song"),
    path("songs/<int:pk>", views.song_detail, name="song_detail"),
    path("artists/", views.show_artists, name="show_artists"),
    path("albums/", views.show_albums, name="show_albums"),
]
