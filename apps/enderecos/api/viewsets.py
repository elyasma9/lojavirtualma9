from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.enderecos.models import Endereco
from .serializers import EnderecossSerializer


class EnderecosViewSet(ModelViewSet):

    serializer_class = EnderecossSerializer

    def get_queryset(self):
        queryset = Endereco.objects.filter(
            user=self.kwargs['usuario_pk']).order_by('id')
        return queryset
