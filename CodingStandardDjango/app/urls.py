from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^input/$', views.input, name='input'),
    url(r'^loading/$', views.loading, name='loading'),
    url(r'^final/$', views.final, name='final')
]