from django.urls import path
from . import views

urlpatterns = [
    # — Anonymous
    path('register/', views.register_view, name='register'),
    path('login/',    views.login_view,    name='login'),
    path('logout/',   views.logout_view,   name='logout'),

    path('',                       views.song_list_view, name='song_list'),
    path('search/',                views.song_search_view, name='song_search'),
    path('songs/<int:song_id>/',   views.song_detail_view, name='song_detail'),

    # — Authenticated User
    path('playlists/',                     views.my_playlists,         name='my_playlists'),
    path('playlists/new/',                 views.create_playlist_view, name='playlist_create'),
    path('playlists/<int:pl_id>/',         views.playlist_detail,      name='playlist_detail'),
    path('playlists/<int:pl_id>/add/<int:song_id>/', views.add_song_to_playlist, name='playlist_add_song'),
    path('playlists/<int:pl_id>/delete/',  views.delete_playlist_view, name='playlist_delete'),
]
