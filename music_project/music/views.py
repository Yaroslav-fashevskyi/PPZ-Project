from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, PlaylistForm
from .models import Song, Playlist

# ————————— Anonymous —————————
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('song_list')
    else:
        form = RegistrationForm()
    return render(request, 'music/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('song_list')
    else:
        form = LoginForm()
    return render(request, 'music/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('song_list')

def song_list_view(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})

def song_search_view(request):
    genre = request.GET.get('genre', '')
    songs = Song.objects.filter(genre__icontains=genre) if genre else Song.objects.none()
    return render(request, 'music/song_search.html', {'songs': songs, 'genre': genre})

def song_detail_view(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'music/song_detail.html', {'song': song})

# ————————— Authenticated User —————————
@login_required
def my_playlists(request):
    playlists = Playlist.objects.filter(owner=request.user)
    return render(request, 'music/my_playlists.html', {'playlists': playlists})

@login_required
def create_playlist_view(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            pl = form.save(commit=False)
            pl.owner = request.user
            pl.save()
            return redirect('playlist_detail', pl.id)
    else:
        form = PlaylistForm()
    return render(request, 'music/playlist_form.html', {'form': form})

@login_required
def playlist_detail(request, pl_id):
    playlist = get_object_or_404(Playlist, pk=pl_id, owner=request.user)
    # всі пісні, яких ще нема у плейлисті
    available_songs = Song.objects.exclude(id__in=playlist.songs.values_list('id', flat=True))
    return render(request, 'music/playlist_detail.html', {
        'playlist': playlist,
        'songs': available_songs,
    })

@login_required
def add_song_to_playlist(request, pl_id, song_id):
    pl = get_object_or_404(Playlist, pk=pl_id, owner=request.user)
    song = get_object_or_404(Song, pk=song_id)
    pl.songs.add(song)
    return redirect('playlist_detail', pl_id)

@login_required
def delete_playlist_view(request, pl_id):
    pl = get_object_or_404(Playlist, pk=pl_id, owner=request.user)
    if request.method == 'POST':
        pl.delete()
        return redirect('my_playlists')
    return render(request, 'music/confirm_delete.html', {'playlist': pl})
