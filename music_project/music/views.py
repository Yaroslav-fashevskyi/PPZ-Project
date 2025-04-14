from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Song, Playlist

def register_view(request):
    """Реєстрація нового користувача."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('song_list')
    else:
        form = UserCreationForm()
    return render(request, 'music/register.html', {'form': form})

def login_view(request):
    """Авторизація (логін) користувача."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('song_list')
    else:
        form = AuthenticationForm()
    return render(request, 'music/login.html', {'form': form})

def logout_view(request):
    """Вихід з облікового запису."""
    logout(request)
    return redirect('song_list')

def song_list(request):
    """Відображення списку всіх пісень."""
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})

def song_detail(request, song_id):
    """Детальна інформація про конкретну пісню."""
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'music/song_detail.html', {'song': song})

def song_search(request):
    """Пошук пісень за жанром."""
    query = request.GET.get('genre', '')
    songs = Song.objects.filter(genre__icontains=query)
    return render(request, 'music/song_search.html', {'songs': songs, 'query': query})

@login_required
def create_playlist(request):
    """Створення нового плейлиста."""
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            playlist = Playlist.objects.create(user=request.user, name=name)
            return redirect('playlist_detail', playlist_id=playlist.id)
    return render(request, 'music/create_playlist.html')

@login_required
def user_playlists(request):
    """Список плейлистів поточного користувача."""
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'music/user_playlists.html', {'playlists': playlists})

@login_required
def playlist_detail(request, playlist_id):
    """Перегляд одного плейлиста (деталі)."""
    playlist = get_object_or_404(Playlist, id=playlist_id, user=request.user)
    songs_in_playlist = playlist.songs.all()
    all_songs = Song.objects.all()
    return render(request, 'music/playlist_detail.html', {
        'playlist': playlist,
        'songs_in_playlist': songs_in_playlist,
        'all_songs': all_songs,
    })

@login_required
def add_song_to_playlist(request, playlist_id, song_id):
    """Додавання пісні до плейлиста."""
    playlist = get_object_or_404(Playlist, id=playlist_id, user=request.user)
    song = get_object_or_404(Song, id=song_id)
    playlist.songs.add(song)
    return redirect('playlist_detail', playlist_id=playlist.id)

@login_required
def delete_playlist(request, playlist_id):
    """Видалення плейлиста."""
    playlist = get_object_or_404(Playlist, id=playlist_id, user=request.user)
    if request.method == 'POST':
        playlist.delete()
        return redirect('user_playlists')
    return render(request, 'music/confirm_delete.html', {'playlist': playlist})
