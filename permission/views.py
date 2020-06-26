from django.shortcuts import render


def permission(request):
    return render(request, 'permission/permission.html')