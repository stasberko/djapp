from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.users, name='users'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^mlogin/$', views.mlogin, name='mlogin'),
    url(r'^mlogout/$', views.mlogout, name='mlogout'),
]
