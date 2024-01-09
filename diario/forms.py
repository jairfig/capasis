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
        self.fields['aluno'].disabled = True


PresencaFormSet = modelformset_factory(Presenca, form=PresencaForm, extra=0)
