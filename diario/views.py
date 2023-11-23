from django.shortcuts import render
from django.http import HttpResponse

from diario.models import Professor
from django.contrib.auth.models import User


# Create your views here.
def meu_diario(request):
    user = User.objects.get(id=3)
    professor = Professor.objects.filter(usuario=user).first()
    turma = professor.turma_set.last()
    context = {
        'turma': turma,
        'professor': professor,
        'aulas': turma.aulaagendada_set.all()
    }
    return render(request, 'diario/meu_diario.html', context)