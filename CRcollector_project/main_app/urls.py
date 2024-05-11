from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.cards_index, name='index'),
    path('cards/<int:card_id>/', views.cards_detail, name='details'),
    path('cards/create/', views.CardCreate.as_view(), name='card_create'),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name="cards_update"),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='cards_delete'),

    path('cards/<int:pk>/add_status/', views.add_status, name='add_status'),
    path('cards/<int:pk>/assoc_player/<int:player_pk>/', views.assoc_player, name='assoc_player'),
    path('cards/<int:pk>/assoc_delete/<int:player_pk>', views.assoc_delete, name='assoc_delete'),


    #Player URLS
    path('players/', views.PlayerList.as_view(), name='players_index'),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name='players_detail'),
    path('players/create/', views.PlayerCreate.as_view(), name="players_create"),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='player_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='player_delete'),
]
