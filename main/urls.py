from django.urls import re_path
from main import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^result$', views.result, name='result'),
    re_path(r'^filter$', views.filter, name='filter'),
]
