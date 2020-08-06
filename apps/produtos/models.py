from django.db import models

# Create your models here.


class Produto(models.Model):

    nome = models.CharField(max_length=45)
    preco = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return '%s: R$ %s' % (self.nome, self.preco)
