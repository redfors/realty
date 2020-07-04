from django.shortcuts import render
from catalog.models import Realty


def search(request):
    last = Realty.objects.filter(published='published')[:3].all()
    data_realty = Realty.objects.filter(published='published')
    return render(request, 'search/search.html', {'data_realty': data_realty, "last": last})
