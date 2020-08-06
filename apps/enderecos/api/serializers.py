from rest_framework.serializers import ModelSerializer
from apps.enderecos.models import Endereco


class EnderecossSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'user', 'logradouro', 'bairro',
                  'cep', 'cidade', 'estado', 'numero')
