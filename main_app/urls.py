from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('synths/', views.synths_index, name="index"),
    path('synths/<int:synth_id>/', views.synth_details, name="details"),
    path('synths/create/', views.SynthCreate.as_view(), name='synths_create'),
    path('synths/<int:pk>/delete/', views.SynthDelete.as_view(), name='synth_delete'),
    path('synths/<int:pk>/update/', views.SynthUpdate.as_view(), name='synth_update'),
    path('synths/<int:synth_id>/add_patch', views.add_patch, name='add_patch'),
    path('artists/', views.ArtistList.as_view(), name="artists_index"),
    path('artists/<int:synth_id>/assoc_artist/<int:artist_id>/', views.assoc_artist, name="assoc_artist"),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='artist_detail'),
    path('artists/create/', views.ArtistCreate.as_view(), name='artists_create'),
    path('artists/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artists_update'),
    path('artists/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist_delete'),
]