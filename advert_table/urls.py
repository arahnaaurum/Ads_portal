from django.urls import path, include
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('', AdsList.as_view(), name = "adslist"),
    path('<int:pk>', AdsDetail.as_view(), name = "adsdetail"),
    path('create/', AdsCreateView.as_view(), name = "ads_add"),
    path('<int:pk>/edit/', AdsUpdateView.as_view(), name = "ads_edit"),
    path('<int:pk>/delete/', AdsDeleteView.as_view(), name = "ads_delete"),
    path('author/', AuthorCreateView.as_view(), name="author"),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name="comment"),
    path('<int:pk>/commentacc/', CommentAcceptView.as_view(), name="comment_accept"),
    path('<int:pk>/commentdel/', CommentDeleteView.as_view(), name="comment_delete"),
]
