from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Song(models.Model):
    title       = models.CharField(max_length=200)
    artist      = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    style       = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    audio_file  = models.FileField(upload_to='songs/', blank=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} — {self.artist}"

class Playlist(models.Model):
    name       = models.CharField(max_length=100)
    owner      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    songs      = models.ManyToManyField(Song, blank=True, related_name='in_playlists')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.owner.username})"
