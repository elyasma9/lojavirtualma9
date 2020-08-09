from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.usuarios.models import CustomUser
from .serializers import UsuariosCompletoSerializer


class UsuariosViewSet(ModelViewSet):

    queryset = CustomUser.objects.filter(is_staff=False).order_by('pk')
    serializer_class = UsuariosCompletoSerializer

    def list(self, request):
        queryset = CustomUser.objects.filter(is_staff=False).order_by('pk')
        serializer = UsuariosCompletoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CustomUser.objects.filter(is_staff=False)
        user = get_object_or_404(queryset, pk=pk)
        serializer = UsuariosCompletoSerializer(user)
        return Response(serializer.data)
