from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(blank=True)  # just a example, don't affect the app
    avatar = models.ImageField('Foto do perfil',
                               upload_to='static/img/',
                               null=True,
                               blank=True)

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')
