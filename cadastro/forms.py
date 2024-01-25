from django import forms
from .models import Arquivo, Pessoa

class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['pessoa', 'arquivo']
        widgets = {
            'pessoa': forms.HiddenInput(),
        }


class ArquivosForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['arquivo']


ArquivoFormSet = forms.inlineformset_factory(Pessoa, Arquivo, form=ArquivosForm, extra=1, can_delete=True)


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome']

