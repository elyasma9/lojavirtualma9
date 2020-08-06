from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from apps.usuarios.api.viewsets import UsuariosViewSet
from apps.enderecos.api.viewsets import EnderecosViewSet


router = routers.DefaultRouter()
router.register('usuarios', UsuariosViewSet)
router.register('enderecos', EnderecosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
