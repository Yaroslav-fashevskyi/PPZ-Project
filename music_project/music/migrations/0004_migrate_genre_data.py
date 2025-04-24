from django.db import migrations

def forwards(apps, schema_editor):
    Song  = apps.get_model('music', 'Song')
    Genre = apps.get_model('music', 'Genre')

    seen = set()
    for song in Song.objects.all():
        old = song.genre
        if old and old not in seen:
            Genre.objects.create(name=old)
            seen.add(old)

    for song in Song.objects.all():
        if song.genre:
            g = Genre.objects.get(name=song.genre)
            song.genre_fk = g
            song.save(update_fields=['genre_fk'])

def backwards(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_genre_song_genre_fk'),
    ]

    operations = [
    ]







