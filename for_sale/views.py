from django.shortcuts import render


def for_sale(request):
    return render(request, 'for_sale/for_sale.html')