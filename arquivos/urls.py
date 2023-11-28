from django.urls import path
from .views import upload_arquivos, detalhes_pessoa

urlpatterns = [
    path('pessoa/<int:pessoa_id>/upload/', upload_arquivos, name='upload_arquivos'),
    path('pessoa/<int:pessoa_id>/', detalhes_pessoa, name='detalhes_pessoa'),

]
