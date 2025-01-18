from django.urls import path
from . import views

urlpatterns = [
    path('', views.ua_map),
]