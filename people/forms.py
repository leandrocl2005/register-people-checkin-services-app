from django import forms
from .models import Person

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit, Row, Column, Field


class PersonForm(forms.ModelForm):
  class Meta:
    model = Person
    fields = '__all__'

  born_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.layout = Layout(
        Fieldset(
            "Identificação",
            Field(
                # identification
                'name',
                'mother_name',
                Row(Column('born_date', css_class='col-md-3'),
                    Column('gender', css_class='col-md-3'),
                    Column('cpf', css_class='col-md-6')),
                Row(Column('rg_ssp', css_class='col-md-3'),
                    Column('rg', css_class="col-md-3")),
            )),
        # address
        Fieldset(
            "Endereço",
            Field(
                'address_line_1',
                Row(
                    Column('neighbourhood', css_class="col-md-9"),
                    Column('address_line_2', css_class="col-md-3"),
                ),
                Row(Column('city', css_class='form-group col-md-6'),
                    Column('state', css_class='form-group col-md-3'),
                    Column('postal_code', css_class='form-group col-md-3'))),
            Field('residence_type', css_class="col-md-2")),
        # contacts
        Fieldset(
            'Contatos',
            Field(
                Row(
                    Column('ddd_private_phone',
                           css_class='form-group col-md-1'),
                    Column('private_phone', css_class='form-group col-md-3')),
                Row(Column('ddd_message_phone',
                           css_class='form-group col-md-1'),
                    Column('message_phone', css_class='form-group col-md-3'),
                    css_class='form-row'),
                'email',
            )),
        Fieldset("Outras informações", Field('observation', rows='4')),
        # submit button
        Submit('submit', 'Enviar'))
