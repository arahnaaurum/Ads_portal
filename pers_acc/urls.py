from django.urls import path
from advert_table.views import *
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, RegisterFinView

urlpatterns = [
    path('', CommentList.as_view(), name="commentlist"),
    path('login/',
         LoginView.as_view(template_name='sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    path('register/',
         RegisterView.as_view(),
         name='register'),
    path('finish/',
         RegisterFinView.as_view(),
         name='registerfin'),

]