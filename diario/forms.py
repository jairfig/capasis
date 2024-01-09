from django import forms
from django.forms import modelformset_factory
from django.forms.widgets import TextInput, CheckboxInput
from .models import Presenca


class ReadOnlyWidget(TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        return value or super().render(name, value, attrs)


class PresencaForm(forms.ModelForm):
    class Meta:
        model = Presenca
        fields = ['aluno', 'presente', 'justificativa']
        widgets = {'presente': forms.CheckboxInput(),
                   # 'aluno': ReadOnlyWidget(attrs={'readonly': 'readonly'}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['aluno'].widget.attrs['readonly'] = 'readonly'
        # self.fields['aluno'].disabled = True

PresencaFormSet = modelformset_factory(Presenca, form=PresencaForm, extra=0)
# PresencaFormSet = modelformset_factory(Presenca, fields=['aluno', 'presente', 'justificativa'], extra=0)
