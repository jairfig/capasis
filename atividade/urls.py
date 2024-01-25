from django.urls import path, include
from atividade import views

urlpatterns = [
    path('', views.atividade, name='atividade'),
    path('adicionar', views.atividadeAdd, name='atividadeAdd'),
    path('form', views.atividadeForm, name='atividadeForm'),
]