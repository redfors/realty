from django.shortcuts import render


def i_rent(request):
    return render(request, 'i_rent/i_rent.html')