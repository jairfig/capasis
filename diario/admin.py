from django.contrib import admin
from .models import Professor, Aluno, Modulo, Turma, AulaAgendada, Presenca

class TurmaInline(admin.TabularInline):
    model = Turma
    extra = 1
    allow_add = False


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'usuario')
    search_fields = ('nome', 'email', 'telefone')

    inlines = [TurmaInline]


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'email', 'telefone')


class ModuloAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'trilha')
    search_fields = ('nome', 'descricao', 'trilha')


class AulasInline(admin.TabularInline):
    model = AulaAgendada
    extra = 1
    allow_add = True


class AlunosInline(admin.TabularInline):
    model = Turma.alunos.through
    extra = 1


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome_turma', 'professor', 'modulo')
    search_fields = ('nome_turma', 'professor', 'modulo')
    exclude = ('alunos', )

    inlines = [AlunosInline, AulasInline, ]


class AulaAdmin(admin.ModelAdmin):
    list_display = ('turma', 'data', 'hora_inicio', 'hora_fim')
    search_fields = ('turma', 'data', 'hora_inicio', 'hora_fim')


class PresencaAdmin(admin.ModelAdmin):
    list_display = ('aula', 'aluno', 'situacao', 'justificativa')
    search_fields = ('aula', 'aluno', 'situacao', 'justificativa')


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Modulo, ModuloAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(AulaAgendada, AulaAdmin)
admin.site.register(Presenca, PresencaAdmin)