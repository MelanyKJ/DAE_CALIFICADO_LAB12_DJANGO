from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^prestamos/$', views.prestamos_list),
    re_path(r'^prestamos/(?P<pk>[0-9]+)/$', views.prestamos_detail),
]