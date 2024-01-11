from django.urls import path, include
from modulo import  views

urlpatterns = [
    path('', views.modulo, name='modulo'),
]