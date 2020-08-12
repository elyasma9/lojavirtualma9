from django.db import models
from usuarios.models import CustomUser


class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             related_name='enderecos')
    logradouro = models.CharField(max_length=80)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    numero = models.CharField(max_length=20)

    def __str__(self):
        return '%s, %s' % (self.cidade, self.logradouro)
