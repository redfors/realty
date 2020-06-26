from django.urls import path

from . import views

urlpatterns = [
    path('', views.for_sale, name='for_sale'),
]