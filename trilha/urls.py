from django.urls import path, include
from trilha import  views

urlpatterns = [
    path('', views.trilha, name='trilha'),
]