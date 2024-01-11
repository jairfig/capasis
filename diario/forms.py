from django import forms
from django.forms import modelformset_factory
from django.forms.widgets import TextInput, CheckboxInput
from .models import Presenca


class PresencaForm(forms.ModelForm):
    class Meta:
        model = Presenca
        fields = ['aluno', 'presente', 'justificativa']
        widgets = {'presente': forms.CheckboxInput(),}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        aluno_nome = self.instance.aluno.nome if self.instance and self.instance.aluno else ''
        self.fields['presente'].label = f"{aluno_nome}:"
        self.fields['aluno'].widget = forms.HiddenInput()



PresencaFormSet = modelformset_factory(Presenca, form=PresencaForm, extra=0)
