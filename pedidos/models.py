from django.db import models
from django.utils import timezone

from usuarios.models import CustomUser
from enderecos.models import Endereco
from produtos.models import Produto


class Pedido(models.Model):

    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="pedido"
    )
    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.SET_NULL,
        related_name="destino",
        null=True,
        blank=True,
    )
    data_pedido = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=16, choices=STATUS_CHOICES, blank=False, null=False
    )
    produtos = models.ManyToManyField(Produto, related_name="carrinho")

    def __str__(self):
        return "%s, esse é o seu carrinho." % (self.user.get_full_name())
