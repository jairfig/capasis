from django.contrib import admin
from .models import Pessoa, Arquivo

# Register your models here.

class ArquivosInline(admin.TabularInline):
    model = Arquivo
    extra = 1


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

    inlines = [ArquivosInline,]


@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'arquivo')
    search_fields = ('pessoa', 'arquivo')

