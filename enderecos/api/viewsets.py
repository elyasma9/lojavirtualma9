from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecossSerializer


class EnderecosViewSet(ModelViewSet):

    serializer_class = EnderecossSerializer

    def get_queryset(self):
        enderecos = Endereco.objects.filter(user=self.kwargs["usuario_pk"])
        queryset = enderecos.order_by("id")
        return queryset
