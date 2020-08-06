from rest_framework.serializers import ModelSerializer
from apps.enderecos.models import Endereco
from apps.usuarios.api.serializers import UsuariosSerializer


class EnderecossSerializer(ModelSerializer):

    user = UsuariosSerializer()

    class Meta:
        model = Endereco
        fields = ('id', 'user', 'logradouro', 'bairro',
                  'cep', 'cidade', 'estado', 'numero')
