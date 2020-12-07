from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat, name='Chat'),
    path('context', views.getcontext, name='ChatContext')
]