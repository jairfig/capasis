from django.urls import path, include
from curso import  views

urlpatterns = [
    path('', views.curso, name='curso'),
]