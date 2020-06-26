from django.urls import path

from . import views

urlpatterns = [
    path('', views.permission, name='permission'),
]