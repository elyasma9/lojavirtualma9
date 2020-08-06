from rest_framework.viewsets import ModelViewSet
from apps.pedidos.models import Pedido
from .serializers import PedidosSerializer


class PedidosViewSet(ModelViewSet):

    queryset = Pedido.objects.all()
    serializer_class = PedidosSerializer
