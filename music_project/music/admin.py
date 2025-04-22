from django.contrib import admin
from .models import Song, Playlist
from django.utils.html import format_html     # <-- обов’язково!


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'genre', 'cover_thumbnail')
    readonly_fields = ('cover_thumbnail',)

    def cover_thumbnail(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="50" style="object-fit: cover;"/>', obj.cover_image.url)
        return '-'
    cover_thumbnail.short_description = 'Обкладинка'

admin.site.register(Playlist)
