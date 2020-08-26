from rest_framework.viewsets import ModelViewSet
from pedidos.models import Pedido
from .serializers import PedidosSerializer


class PedidosViewSet(ModelViewSet):

    serializer_class = PedidosSerializer

    def get_queryset(self):
        queryset = Pedido.objects.filter(user=self.kwargs["usuario_pk"])
        return queryset
