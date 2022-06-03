"""Music app views"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Song, Artist, Album


@login_required
def show_songs(request):
    """Muestra las canciones"""
    songs = Song.objects.all()
    return render(request, "music/show-songs.html", {"songs": songs})


@login_required
def song_detail(request, pk):
    """Muestra una canción en específico"""
    song = Song.objects.get(pk=pk)
    return render(request, "music/song-detail.html", {"song": song})


@login_required
def create_artist(request):
    """Crea un artista"""
    if request.method == "POST":
        name = request.POST["name"]
        birthday = request.POST.get("birthday")
        artist = Artist(name=name, birthday=birthday)
        artist.save()
        return redirect("music:show_songs")
    else:
        return render(request, "music/create-artist.html",)


@login_required
def create_song(request):
    """Crea un artista"""
    if request.method == "POST":
        title = request.POST["title"]
        artist_id = request.POST["artist_id"]
        album_id = request.POST["album_id"]
        song = Song(title=title, artist_id=artist_id, album_id=album_id)
        song.save()
        return redirect("music:show_songs")
    else:
        artists = Artist.objects.all()
        albums = Album.objects.all()
        return render(request, "music/create-song.html", {"artists": artists, "albums": albums})


@login_required
def show_artists(request):
    """Muestra los artistas"""
    artists = Artist.objects.all()
    return render(request, "music/show-artists.html", {"artists": artists})


@login_required
def show_albums(request):
    """Muestra los álbumes"""
    albums = Album.objects.all()
    return render(request, "music/show-albums.html", {"albums": albums})
