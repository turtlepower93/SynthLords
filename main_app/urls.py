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
]