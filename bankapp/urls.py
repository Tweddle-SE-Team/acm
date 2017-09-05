from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^account', views.account, name='account'),
    url(r'^$', views.index, name='index')
]