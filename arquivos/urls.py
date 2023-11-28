from django.urls import path
from .views import upload_arquivos, detalhes_pessoa, lista_pessoas, cadastra_pessoa

urlpatterns = [
    path('<int:pessoa_id>/upload/', upload_arquivos, name='upload_arquivos'),
    path('<int:pessoa_id>/', detalhes_pessoa, name='detalhes_pessoa'),
    path('', lista_pessoas, name='lista_pessoas'),
    path('add/', cadastra_pessoa, name='cadastra_pessoa'),
]
