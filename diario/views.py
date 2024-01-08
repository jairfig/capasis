from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from diario.models import Professor, AulaAgendada
from django.contrib.auth.models import User


# Create your views here.
def meu_diario(request):
    try:
        user = User.objects.get(id=2)
        professor = Professor.objects.filter(usuario=user).first()
        turma = professor.turma_set.last()

        if not turma:
            raise Professor.DoesNotExist("Turma não encontrada para este professor")

        aulas = turma.aulaagendada_set.all()

        if not aulas:
            raise AulaAgendada.DoesNotExist("Aulas não encontradas para esta turma")

        if request.method == 'POST':
            chamada = aulas.filter(id=request.POST.get('aula_id')).first()
        else:
            chamada = aulas.filter(data=timezone.now()).first()

        context = {
            'turma': turma,
            'professor': professor,
            'aulas': aulas,
            'chamada': chamada,
        }

        return render(request, 'diario/meu_diario.html', context)

    except Professor.DoesNotExist as e:
        return HttpResponse(f"Erro: {str(e)}")

    except AulaAgendada.DoesNotExist as e:
        return HttpResponse(f"Erro: {str(e)}")
