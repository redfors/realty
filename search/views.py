from django.shortcuts import render
from catalog.models import Realty


def search(request):
    if request.is_ajax():
        test = request.GET.get('price')
        print(test)
        data_realty = Realty.objects.filter(published='draft')
        return render(request, 'search/search.html', {'data_realty': data_realty})
        # type = Profile.objects.get(user=user)
        # type.type_user = typeUser

    last = Realty.objects.filter(published='published')[:3].all()
    data_realty = Realty.objects.filter(published='published')
    return render(request, 'search/search.html', {'data_realty': data_realty, "last": last})
