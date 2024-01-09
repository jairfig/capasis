from django.urls import path, include
from atividade import views

urlpatterns = [
    path('', views.atividade, name='atividade'),
]