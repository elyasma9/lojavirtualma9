from rest_framework.viewsets import ModelViewSet
from apps.produtos.models import Produto
from .serializers import ProdutosSerializer


class ProdutosViewSet(ModelViewSet):

    queryset = Produto.objects.all()
    serializer_class = ProdutosSerializer
