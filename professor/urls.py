from django.urls import path, include
from professor import  views

urlpatterns = [
    path('', views.professor, name='professor'),
]