from rest_framework.viewsets import ModelViewSet
from apps.usuarios.models import CustomUser
from .serializers import UsuariosSerializer

class UsuariosViewSet(ModelViewSet):

    queryset = CustomUser.objects.filter(is_staff=False)
    serializer_class = UsuariosSerializer
