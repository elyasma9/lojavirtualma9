from rest_framework.serializers import ModelSerializer
from apps.usuarios.models import CustomUser


class UsuariosSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'nome', 'email')
