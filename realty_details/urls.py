from django.urls import path

from . import views

urlpatterns = [

    path('<slug:slug>/', views.RealtyDetails.as_view(), name='realty_details'),
]
