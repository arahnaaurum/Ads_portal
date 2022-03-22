"""advert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from ckeditor_uploader.views import upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fpages/', include('django.contrib.flatpages.urls')),
    path('ads/', include('advert_table.urls')),
    # path('accounts/', include('allauth.urls')),
    path('personal/', include('pers_acc.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditor/upload/', login_required(upload), name='ckeditor_upload'),
]