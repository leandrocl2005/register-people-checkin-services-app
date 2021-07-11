from django.db import models

from .brasilian_states_list import states as STATE_CHOICES
from .brasilian_ddds_list import ddds as DDD_CHOICES

from .validators import (check_cep, check_city, check_cpf, check_phone)


class Person(models.Model):
  name = models.CharField(max_length=100, verbose_name='Nome')
  mother_name = models.CharField(max_length=100,
                                 blank=True,
                                 null=True,
                                 verbose_name='Nome da mãe')
  born_date = models.DateField(blank=True,
                               null=True,
                               help_text="Exemplo: 03/12/2015",
                               verbose_name='Dt. nascimento')
  email = models.EmailField(max_length=100,
                            blank=True,
                            null=True,
                            unique=True,
                            verbose_name='E-mail')
  GENDER_CHOICES = [
      ('M', 'Masculino'),
      ('F', 'Feminino'),
      ('O', 'Outro'),
  ]
  gender = models.CharField(max_length=1,
                            choices=GENDER_CHOICES,
                            blank=True,
                            null=True,
                            verbose_name='Gênero')
  cpf = models.CharField(max_length=14,
                         blank=True,
                         null=True,
                         unique=True,
                         help_text='Exemplo: 00000000000',
                         verbose_name='CPF',
                         validators=[check_cpf])

  rg = models.CharField(max_length=14,
                        blank=True,
                        null=True,
                        verbose_name='RG')
  rg_ssp = models.CharField(max_length=2,
                            choices=STATE_CHOICES,
                            blank=True,
                            null=True,
                            verbose_name='SSP')

  state = models.CharField(max_length=2,
                           choices=STATE_CHOICES,
                           blank=True,
                           null=True,
                           verbose_name='Estado')
  address_line_1 = models.CharField(max_length=100,
                                    blank=True,
                                    null=True,
                                    help_text='Rua e número da residência',
                                    verbose_name='Rua e número da residência')
  address_line_2 = models.CharField(max_length=100,
                                    blank=True,
                                    null=True,
                                    help_text='apartamento, bloco,...',
                                    verbose_name='Complemento')
  neighbourhood = models.CharField(max_length=60,
                                   blank=True,
                                   null=True,
                                   verbose_name='Bairro')
  city = models.CharField(max_length=60,
                          blank=True,
                          null=True,
                          verbose_name="Cidade",
                          validators=[check_city])
  postal_code = models.CharField(max_length=15,
                                 blank=True,
                                 null=True,
                                 help_text='Exemplo: 00000000',
                                 verbose_name="CEP",
                                 validators=[check_cep])
  RESIDENCE_TYPE_CHOICES = [('urban', 'Urbano'), ('rural', 'Rural')]
  residence_type = models.CharField(max_length=6,
                                    choices=RESIDENCE_TYPE_CHOICES,
                                    blank=True,
                                    null=True,
                                    verbose_name='Distrito')
  ddd_private_phone = models.CharField(max_length=2,
                                       blank=True,
                                       null=True,
                                       choices=DDD_CHOICES,
                                       verbose_name="DDD")
  private_phone = models.CharField(max_length=10,
                                   blank=True,
                                   null=True,
                                   help_text='Exemplo: 999999999',
                                   verbose_name='Tel. p/ contato',
                                   validators=[check_phone])
  ddd_message_phone = models.CharField(max_length=2,
                                       blank=True,
                                       null=True,
                                       choices=DDD_CHOICES,
                                       verbose_name="DDD")
  message_phone = models.CharField(max_length=10,
                                   blank=True,
                                   null=True,
                                   help_text='Exemplo: 999999999',
                                   verbose_name='Tel. p/ mensagem',
                                   validators=[check_phone])

  created_at = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Criado em")
  updated_at = models.DateTimeField(auto_now=True,
                                    verbose_name="Atualizado em")

  observation = models.TextField(max_length=600,
                                 blank=True,
                                 null=True,
                                 verbose_name='Observação')

  class Meta:
    verbose_name_plural = "Pessoas"
    verbose_name = "Pessoa"
    ordering = ('name', )

  @property
  def formatted_created_at(self):
    return self.created_at.strftime("%d/%m/%Y")

  @property
  def formatted_updated_at(self):
    return self.updated_at.strftime("%d/%m/%Y")

  @property
  def formatted_born_date(self):
    if self.born_date:
      return self.born_date.strftime("%d/%m/%Y")

  @property
  def formatted_cpf(self):
    if self.cpf:
      return "{}.{}.{}-{}".format(self.cpf[:3], self.cpf[3:6], self.cpf[6:9],
                                  self.cpf[9:11])

  @property
  def formatted_postal_code(self):
    if self.postal_code:
      return "{}-{}".format(self.postal_code[:5], self.postal_code[5:9])

  def __str__(self):
    return self.name + "  -  (dt. nasc.: " + self.born_date.strftime(
        "%d/%m/%Y") + ")"
