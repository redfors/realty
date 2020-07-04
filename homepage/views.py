from django.shortcuts import render
from catalog.models import Realty


def homepage(request):
    data_realty = Realty.objects.filter(published='published')[:4].all()
    return render(request, 'homepage/index.html', {'data_realty': data_realty})
