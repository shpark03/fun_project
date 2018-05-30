from django.conf.urls import include, url
from . import views

urlpatterns =  [
        url(r'^http_response/$', views.http_response, name='http_response'),
        url(r'^simple_template/$', views.simple_template, name='simple_template'),
        url(r'^users/$', views.users, name='users'),
        url(r'^json_response/', views.json_response, name='json_response'),
        ]
