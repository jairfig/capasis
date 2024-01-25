from django.contrib import admin

from django.contrib import admin
from .models import Pessoa, Arquivo


class ArquivosInline(admin.TabularInline):
    model = Arquivo
    extra = 1

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

    inlines = [ArquivosInline,]
