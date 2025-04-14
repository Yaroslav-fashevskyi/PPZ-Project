from django.urls import path
from . import views

urlpatterns = [
    # Анонімний доступ
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Сторінка зі списком пісень (головна)
    path('', views.song_list, name='song_list'),

    # Детальна сторінка пісні
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),

    # Пошук пісень за жанром
    path('search/', views.song_search, name='song_search'),

    # Плейлисти користувача
    path('playlists/', views.user_playlists, name='user_playlists'),

    # Створення та деталі плейлиста
    path('playlist/create/', views.create_playlist, name='create_playlist'),
    path('playlist/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),

    # Видалення плейлиста
    path('playlist/<int:playlist_id>/delete/', views.delete_playlist, name='delete_playlist'),

    # Додавання пісні до плейлиста
    path('playlist/<int:playlist_id>/add_song/<int:song_id>/', views.add_song_to_playlist, name='add_song_to_playlist'),
]

