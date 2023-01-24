from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from ckeditor_uploader.views import upload

urlpatterns = [
    path('', include('index.urls')),
    path('admin/', admin.site.urls),
    path('fpages/', include('django.contrib.flatpages.urls')),
    path('ads/', include('advert_table.urls')),
    # path('accounts/', include('allauth.urls')),
    path('personal/', include('pers_acc.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditor/upload/', login_required(upload), name='ckeditor_upload'),
]