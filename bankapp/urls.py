from django.conf.urls import url

from . import views
app_name = 'bankapp'
urlpatterns = [
    url(r'^login', views.submitLogin, name='login'),
    url(r'^logout', views.submitLogout, name='logout'),
    url(r'^register', views.register, name='register'),
    url(r'^submit', views.submitRegistration, name='submit'),
    url(r'^question', views.submitQuestion, name='question'),
    url(r'^transfer', views.submitTransfer, name='transfer'),
    url(r'^(?P<username>\w+)/account/$', views.account, name='account'),
    url(r'^$', views.index, name='index')
]