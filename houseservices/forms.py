from crispy_forms.helper import FormHelper
from django import forms
from .models import HouseServices
from crispy_forms.layout import Fieldset, Layout, Submit, Row, Column, Field


class HouseServicesForm(forms.ModelForm):
  class Meta:
    model = HouseServices
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    instance = getattr(self, 'instance', None)
    if instance and instance.pk:
      self.fields['person'].widget.attrs['readonly'] = True
      self.fields['person'].disabled = True

    self.fields['person'].label = "Nome"

    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.layout = Layout(
        Fieldset(
            "Identificação da pessoa",
            Field('person'),
        ),
        Fieldset(
            "Serviços",
            Row(Column('breakfast', css_class="md-3 mb-0"),
                Column('lunch', css_class="md-3 mb-0"),
                Column('snack', css_class="md-3 mb-0")),
            Row(Column('dinner', css_class="md-3 mb-0"),
                Column('shower', css_class="md-3 mb-0"),
                Column('sleep', css_class="md-3 mb-0")),
        ), Submit('submit', 'Enviar'))
