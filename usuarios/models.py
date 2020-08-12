from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    id = models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    telefone = models.CharField(max_length=12)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'sobrenome', 'cpf', 'rg', 'telefone']

    objects = CustomUserManager()

    def __str__(self):
        return '%s %s' % (self.nome, self.sobrenome)

    def get_full_name(self):
        return '%s %s' % (self.nome, self.sobrenome)
