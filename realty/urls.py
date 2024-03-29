"""realty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Slovenia-realty admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('catalog/', include('catalog.urls')),
    path('search/', include('search.urls')),
    path('request/', include('request.urls')),
    path('create/', include('create.urls')),
    path('permission/', include('permission.urls')),
    path('insurance/', include('insurance.urls')),
    path('i_rent/', include('i_rent.urls')),
    path('for_rent/', include('for_rent.urls')),
    path('for_sale/', include('for_sale.urls')),
    path('company/', include('company.urls')),
    path('slovenia/', include('slovenia.urls')),
    path('news/', include('news.urls')),
    path('faq/', include('faq.urls')),
    path('contacts/', include('contacts.urls')),
    path('realty_details/', include('realty_details.urls')),
    path('', include('homepage.urls')),
    path('index/', include('homepage.urls')),
]

if settings.DEBUG == False:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Эта строка опциональна и будет добавлять url'ы только при DEBUG = True

# urlpatterns += staticfiles_urlpatterns()
