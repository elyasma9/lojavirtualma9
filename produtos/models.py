from django.db import models


class Produto(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    preco = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return "%s" % self.nome

    @property
    def get_nome_preco(self):
        return "%s: R$ %s" % (self.nome, self.preco)
