from django.shortcuts import render
from catalog.models import Realty, Images
from django.views.generic.base import View

class RealtyDetails(View):

    def get(self, request, slug):
        data_realty = Realty.objects.get(url=slug)
        images = Images.objects.filter(photos__url=slug)
        return render(request, 'realty_details/realty_details.html', {'data_realty': data_realty, 'images' : images})

