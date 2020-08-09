from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.pedidos.models import Pedido
from .serializers import PedidosSerializer


class PedidosViewSet(ModelViewSet):

    serializer_class = PedidosSerializer

    def get_queryset(self):
        queryset = Pedido.objects.filter(user=self.kwargs['usuario_pk'])
        return queryset
