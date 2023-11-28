from django.shortcuts import render, redirect
from .models import Pessoa, Arquivo
from .forms import ArquivoForm

def upload_arquivos(request, pessoa_id):
    pessoa = Pessoa.objects.get(pk=pessoa_id)

    if request.method == 'POST':
        form = ArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = form.save(commit=False)
            arquivo.pessoa = pessoa
            arquivo.save()
            return redirect('detalhes_pessoa', pessoa_id=pessoa_id)
    else:
        form = ArquivoForm(initial={'pessoa': pessoa_id})

    return render(request, 'arquivos/upload_arquivos.html', {'form': form, 'pessoa': pessoa})


def detalhes_pessoa(request, pessoa_id):
    pessoa = Pessoa.objects.get(pk=pessoa_id)
    arquivos = pessoa.arquivo_set.all()  # Obtém todos os arquivos associados a essa pessoa

    return render(request, 'arquivos/detalhes_pessoa.html', {'pessoa': pessoa, 'arquivos': arquivos})