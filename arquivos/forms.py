from django import forms
from .models import Arquivo

class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['pessoa', 'arquivo']
        widgets = {
            'pessoa': forms.HiddenInput(),
        }