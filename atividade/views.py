from django.shortcuts import render

# Create your views here.
def atividade(request):
    return render(request, 'atividade.html')

def atividadeAdd(request):
    return render(request, 'atividadeAdd.html')

def atividadeForm(request):
    return render(request, 'atividadeForm.html')