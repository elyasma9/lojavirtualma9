from rest_framework.serializers import ModelSerializer
from apps.pedidos.models import Pedido
from apps.usuarios.api.serializers import UsuariosSerializer
from apps.enderecos.api.serializers import EnderecossSerializer
from apps.produtos.api.serializers import ProdutosSerializer

class PedidosSerializer(ModelSerializer):
    user = UsuariosSerializer()
    endereco = EnderecossSerializer()
    produtos = ProdutosSerializer(many=True)

    class Meta:

        model = Pedido
        fields = ('id', 'user', 'endereco',
                  'produtos', 'status', 'data_pedido')
