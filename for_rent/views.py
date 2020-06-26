from django.shortcuts import render


def for_rent(request):
    return render(request, 'for_rent/for_rent.html')