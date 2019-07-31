"""Algerate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    path('rate/', views.rate, name='rate'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('image_list/', views.images_list, name='image_list'),
    path('post/<uuid>', views.image_details, name='post'),
    path('verify/', views.verified_page, name='verified'),
    path('get_image/mode=<int:mode>', views.get_image, name='get_image'),
    path('rate_image/<int:rate>', views.rate_image, name='rate_image'),
    path('submit_photo/', views.submit_photo, name='submit_photo'),
    path('no_images/', views.no_images, name='no_images')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
