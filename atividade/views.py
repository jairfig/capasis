from django.shortcuts import render

# Create your views here.
def atividade(request):
    return render(request, 'atividade.html')