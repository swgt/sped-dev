from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^upload/$', views.upload),
    url(r'^upload$', views.upload_file),
]