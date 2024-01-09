from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from diario.models import Professor, Aula, Presenca, Aluno
from django.contrib.auth.models import User
from .forms import PresencaForm, PresencaFormSet


# Create your views here.
def meu_diario(request):
    try:
        user = User.objects.get(id=2)
        professor = Professor.objects.filter(usuario=user).first()
        turma = professor.turma_set.last()

        if not turma:
            raise Professor.DoesNotExist("Turma não encontrada para este professor")

        aulas = turma.aula_set.all()

        if not aulas:
            raise Aula.DoesNotExist("Aulas não encontradas para esta turma")

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

    except Aula.DoesNotExist as e:
        return HttpResponse(f"Erro: {str(e)}")


def lancar_presencas(request, aula_agendada_id):
    aula = Aula.objects.get(pk=aula_agendada_id)
    alunos = Aluno.objects.filter(turma=aula.turma)

    PresencaFormSet = forms.modelformset_factory(Presenca, form=PresencaForm, extra=0)

    if request.method == 'POST':
        formset = PresencaFormSet(request.POST, queryset=Presenca.objects.filter(aula=aula))
        if formset.is_valid():
            formset.save()
            context = {
                'aula': aula,
                'message': 'Presenças lançadas com sucesso!'
            }
            return render(request, 'diario/meu_diario.html', context)
    else:
        formset = PresencaFormSet(queryset=Presenca.objects.filter(aula=aula))

    return render(request, 'diario/meu_diario.html', {'formset': formset, 'aula_agendada': aula})


def presenca(request, id_aula):
    aula = get_object_or_404(Aula, pk=id_aula)
    presencas = Presenca.objects.filter(aula=aula)
    alunos = Aluno.objects.filter(turma=aula.turma)

    if request.method == 'POST':
        formset = PresencaFormSet(request.POST, queryset=presencas)
        if formset.is_valid():
            formset.save()
            return redirect('meu_diario')
    else:
        formset = PresencaFormSet(queryset=presencas)

    return render(request, 'diario/presencas.html', {'aula': aula, 'formset': formset})

