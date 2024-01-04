from django.urls import path, include
from atividade.views import atividade

urlpatterns = [
    path('', atividade, name='atividade'),
]