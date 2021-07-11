from django.db import models
from django.urls import reverse

from people.models import Person


class HouseServices(models.Model):
    class Meta:
        verbose_name_plural = "Serviços da casa"
        verbose_name = "Serviço da casa"

    person = models.ForeignKey(Person,
                               on_delete=models.PROTECT,
                               verbose_name="Pessoa")

    breakfast = models.BooleanField(default=False,
                                    blank=True,
                                    verbose_name="Café da manhã")
    lunch = models.BooleanField(default=False,
                                blank=True,
                                verbose_name="Almoço")
    snack = models.BooleanField(default=False,
                                blank=True,
                                verbose_name="Lanche da tarde")
    dinner = models.BooleanField(default=False,
                                 blank=True,
                                 verbose_name="Jantar")
    shower = models.BooleanField(default=False,
                                 blank=True,
                                 verbose_name="Banho")
    sleep = models.BooleanField(default=False,
                                blank=True,
                                verbose_name="Per noite")

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="Atualizado em")

    @property
    def person_name(self):
        return self.person.name

    def get_absolute_url(self):
        return reverse("houseservices:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.person.name + "[C:{},A:{},L:{},J:{},B:{},P:{}]".format(
            self.breakfast, self.lunch, self.snack, self.dinner, self.shower,
            self.sleep)
