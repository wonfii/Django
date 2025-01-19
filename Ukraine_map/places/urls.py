from django.urls import path
from . import views

urlpatterns = [
    path('', views.ua_map),
    path('create/', views.create),
    path('delete/<str:name>/', views.delete),
    path('edit/<str:name>/', views.edit),
]