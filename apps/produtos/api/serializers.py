from rest_framework.serializers import ModelSerializer
from apps.produtos.models import Produto


class ProdutosSerializer(ModelSerializer):
    class Meta:

        model = Produto
        fields = ('id', 'nome', 'preco')
