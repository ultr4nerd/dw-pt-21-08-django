from django.shortcuts import render

from .models import Song


def show_songs(request):
    """Muestra las canciones"""
    songs = Song.objects.all()
    return render(request, "music/index.html", {"songs": songs})


def show_artists(request):
    """Muestra los artistas"""


def show_albums(request):
    """Muestra los álbumes"""
