from django.urls import path, include
from diario.views import meu_diario

urlpatterns = [
    path('', meu_diario, name='meu_diario'),
]