from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.usuarios.models import CustomUser
from .serializers import UsuariosCompletoSerializer, UsuariosSerializer
from .serializers import UsuariosChangePasswordSerializer


class UsuariosViewSet(ModelViewSet):

    queryset = CustomUser.objects.filter(is_staff=False).order_by('pk')
    serializer_class = UsuariosCompletoSerializer

    def list(self, request):
        queryset = CustomUser.objects.filter(is_staff=False).order_by('pk')
        serializer = UsuariosSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CustomUser.objects.filter()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UsuariosCompletoSerializer(user)
        return Response(serializer.data)

    @action(detail=True, methods=["POST"])
    def set_password(self, request, pk):
        user = self.get_object()
        serializer = UsuariosChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'Senha alterada com sucesso!'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
