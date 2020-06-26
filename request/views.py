from django.shortcuts import render


def request(request):
    return render(request, 'request/request.html')