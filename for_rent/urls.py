from django.urls import path

from . import views

urlpatterns = [
    path('', views.for_rent, name='for_rent'),
]