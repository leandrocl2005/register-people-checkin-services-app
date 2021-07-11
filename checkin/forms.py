from django import forms
from .models import ChangeCompanion, OtherPeopleCheckin, PatientCheckin

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit, Row, Column, Field


class PatientCheckinForm(forms.ModelForm):
  class Meta:
    model = PatientCheckin
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    instance = getattr(self, 'instance', None)
    self.fields['companion'].required = True
    if instance and instance.pk:
      self.fields['person'].widget.attrs['readonly'] = True
      self.fields['person'].disabled = True
      self.fields['companion'].widget.attrs['readonly'] = True
      self.fields['companion'].disabled = True
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.fields['person'].label = "Paciente"
    self.helper.layout = Layout(
        Field('person'), Field('companion'), Field('active', type="hidden"),
        Fieldset(
            'Motivo do checkin',
            Row(Column('chemotherapy', css_class="md-3 mb-0"),
                Column('surgery', css_class="md-3 mb-0"),
                Column('appointment', css_class="md-3 mb-0")),
            Row(
                Column('radiotherapy', css_class="md-3 mb-0"),
                Column('exams', css_class="md-3 mb-0"),
                Column('other', css_class="md-3 mb-0"),
            )), Field('observation', rows='4'), Submit('submit', 'Enviar'))


class OtherPeopleCheckinForm(forms.ModelForm):
  class Meta:
    model = OtherPeopleCheckin
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    instance = getattr(self, 'instance', None)
    if instance and instance.pk:
      self.fields['person'].widget.attrs['readonly'] = True
      self.fields['person'].disabled = True
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.layout = Layout(Field('person'), Field('active',
                                                       type="hidden"),
                                Field('reason'), Field('observation',
                                                       rows='4'),
                                Submit('submit', 'Enviar'))


class ChangeCompanionForm(forms.ModelForm):
  class Meta:
    model = ChangeCompanion
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(ChangeCompanionForm, self).__init__(*args, **kwargs)
    self.fields['checkin'].queryset = PatientCheckin.objects.filter(
        active=True)
    self.fields['checkin'].label = "Paciente"
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.layout = Layout(Field('checkin'), Field('new_companion'),
                                Submit('submit', 'Enviar'))
