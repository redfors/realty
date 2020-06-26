from django.urls import path

from . import views

urlpatterns = [
    path('', views.i_rent, name='i_rent'),
]