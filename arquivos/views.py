from django.shortcuts import render, redirect
from .models import Pessoa, Arquivo
from .forms import ArquivoFormSet, PessoaForm, ArquivoForm


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

    return render(request, 'arquivos/adicionar.html', {'form': form, 'pessoa': pessoa})


def detalhes_pessoa(request, pessoa_id):
    pessoa = Pessoa.objects.get(pk=pessoa_id)
    arquivos = pessoa.arquivo_set.all()  # Obtém todos os arquivos associados a essa pessoa

    return render(request, 'arquivos/detalhes.html', {'pessoa': pessoa, 'arquivos': arquivos})


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'arquivos/lista.html', {'pessoas': pessoas})


def cadastra_pessoa(request):


    if request.method == 'POST':
        pessoa_form = PessoaForm(request.POST)
        formset = ArquivoFormSet(request.POST, request.FILES, instance=Pessoa())
        if formset.is_valid() and pessoa_form.is_valid():
            pessoa = pessoa_form.save()
            formset.instance = pessoa
            formset.save()
            return render(request, 'arquivos/detalhes.html', {'pessoa': pessoa, 'arquivos': pessoa.arquivo_set.all()})
    else:
        pessoa_form = PessoaForm()
        formset = ArquivoFormSet(instance=Pessoa())

    return render(request, 'arquivos/cadastrar.html', {'arquivos_form': formset, 'pessoa_form': pessoa_form})
