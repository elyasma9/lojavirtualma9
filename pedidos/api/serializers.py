from rest_framework.serializers import ModelSerializer
from pedidos.models import Pedido


class PedidosSerializer(ModelSerializer):
    class Meta:

        model = Pedido
        fields = ("id", "user", "produtos", "status", "endereco", "data_pedido")
