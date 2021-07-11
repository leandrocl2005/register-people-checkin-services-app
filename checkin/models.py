from django.db import models
from people.models import Person


class Checkin(models.Model):
  person = models.ForeignKey(Person,
                             verbose_name='Pessoa',
                             related_name='person',
                             on_delete=models.PROTECT)

  observation = models.TextField("Observação",
                                 max_length=600,
                                 blank=True,
                                 null=True)

  active = models.BooleanField("Ativo", default=True)

  created_at = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Criado em")
  updated_at = models.DateTimeField(auto_now=True,
                                    verbose_name="Atualizado em")


class PatientCheckin(Checkin):
  class Meta:
    verbose_name_plural = "Check-in's de paciente"
    verbose_name = "Check-in de paciente"
    ordering = ['-created_at']

  companion = models.ForeignKey(Person,
                                blank=True,
                                null=True,
                                related_name='companion',
                                verbose_name='Acompanhante',
                                on_delete=models.PROTECT)

  chemotherapy = models.BooleanField(default=False,
                                     verbose_name='Quimioterapia')
  radiotherapy = models.BooleanField(default=False,
                                     verbose_name='Radioterapia')
  surgery = models.BooleanField(default=False, verbose_name='Cirurgia')
  exams = models.BooleanField(default=False, verbose_name='Exames')
  appointment = models.BooleanField(default=False, verbose_name='Consultas')
  other = models.BooleanField(default=False, verbose_name='Outros')

  ca_number = models.CharField(max_length=20,
                               blank=True,
                               null=True,
                               verbose_name='Número C.A.')

  social_vacancy = models.BooleanField(blank=True,
                                       null=True,
                                       verbose_name="Vaga Social?")

  @property
  def companion_name(self):
    if self.companion:
      return self.companion.name

  @property
  def person_name(self):
    return self.person.name

  def __str__(self):
    return self.person.name + " " + self.created_at.strftime(
        "(Entrada em %d/%m/%Y %H:%M)")


class CompanionCheckin(Checkin):
  class Meta:
    verbose_name_plural = "Check-in's de acompanhante"
    verbose_name = "Check-in de acompanhante"
    ordering = ['-created_at']

  patient = models.ForeignKey(Person,
                              related_name='patient',
                              verbose_name='Paciente',
                              on_delete=models.PROTECT)

  def __str__(self):
    return self.person.name + " " + self.created_at.strftime(
        "(Entrada em %d/%m/%Y %H:%M)")


class OtherPeopleCheckin(Checkin):
  class Meta:
    verbose_name_plural = "Check-in's de outras pessoas"
    verbose_name = "Check-in de outras pessoas"
    ordering = ['-created_at']

  REASON_CHOICES = [('professional', 'Profissional'),
                    ('voluntary', 'Voluntário'), ('visitor', 'Visitante'),
                    ('other', 'Outro')]

  reason = models.CharField(max_length=12,
                            choices=REASON_CHOICES,
                            verbose_name='Tipo de check-in')

  def __str__(self):
    return self.person.name + " " + self.created_at.strftime(
        "(Entrada em %d/%m/%Y %H:%M)")


class ChangeCompanion(models.Model):
  checkin = models.ForeignKey(PatientCheckin,
                              verbose_name='Checkin de paciente',
                              related_name='checkin',
                              on_delete=models.PROTECT)
  new_companion = models.ForeignKey(Person,
                                    verbose_name="Novo acompanhante",
                                    related_name='new_companion',
                                    on_delete=models.PROTECT)
  created_at = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Criado em")
  updated_at = models.DateTimeField(auto_now=True,
                                    verbose_name="Atualizado em")

  def __str__(self):
    return self.checkin.companion.name + " -> " + self.new_companion.name + \
        " " + self.created_at.strftime("(Trocado em %d/%m/%Y %H:%M)")
