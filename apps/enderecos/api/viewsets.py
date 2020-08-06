from rest_framework.viewsets import ModelViewSet
from apps.enderecos.models import Endereco
from .serializers import EnderecossSerializer


class EnderecosViewSet(ModelViewSet):

    queryset = Endereco.objects.all()
    serializer_class = EnderecossSerializer
