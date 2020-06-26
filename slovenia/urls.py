from django.urls import path

from . import views

urlpatterns = [
    path('', views.slovenia, name='slovenia'),
]