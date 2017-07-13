from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.chat, name='chat'),
    url(r'^rcv_message$',views.receive_message, name='rcv_message'),
    url(r'^mess_liad$',views.mess_liad, name='mess_liad'),

]