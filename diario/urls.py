from django.urls import path, include
from diario import views

urlpatterns = [
    path('', views.meu_diario, name='meu_diario'),
    path('presenca/<int:id_aula>', views.presenca, name='presenca'),
    path('atividades/', views.atividades, name='atividade'),
]