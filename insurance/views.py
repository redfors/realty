from django.shortcuts import render


def insurance(request):
    return render(request, 'insurance/insurance.html')