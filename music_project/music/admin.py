from django.contrib import admin
from django.utils.html import format_html
from .models import Genre, Song, Playlist

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display   = ('name',)
    search_fields  = ('name',)
    ordering       = ('name',)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display   = ('title', 'artist', 'genre', 'cover_thumbnail')
    readonly_fields= ('cover_thumbnail',)
    list_filter    = ('genre',)
    search_fields  = ('title', 'artist', 'genre__name')

    def cover_thumbnail(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" width="50" style="object-fit:cover" />',
                obj.cover_image.url
            )
        return '-'
    cover_thumbnail.short_description = 'Обкладинка'

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display   = ('name', 'owner', 'created_at')
    search_fields  = ('name', 'owner__username')
    list_filter    = ('owner',)
