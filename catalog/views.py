from django.shortcuts import render
from .models import Realty

def catalog(request):
    data_realty = Realty.objects.filter(published='published')
    return render(request, 'catalog/catalog.html', {'data_realty': data_realty})