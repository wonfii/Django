from django.urls import path
from details import views

urlpatterns = [
    path('about/', views.about),
    path('artworks/', views.artworks),
]