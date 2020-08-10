from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework_nested import routers
from apps.usuarios.api.viewsets import UsuariosViewSet
from apps.usuarios.api.viewsets import UsuariosChangePasswordViewSet
from apps.enderecos.api.viewsets import EnderecosViewSet
from apps.produtos.api.viewsets import ProdutosViewSet
from apps.pedidos.api.viewsets import PedidosViewSet


router = routers.DefaultRouter()

# rota de usuários --> nível 1
router.register('usuarios', UsuariosViewSet, base_name='usuarios')
router.register('produtos', ProdutosViewSet, base_name='produtos')

# rota de usuario aninhada com (endereços, pedidos) --> nível 2
usuario_router = routers.NestedSimpleRouter(
    router, 'usuarios', lookup='usuario')
usuario_router.register(
    'changepassword', UsuariosChangePasswordViewSet, base_name='changepassword')
usuario_router.register('enderecos', EnderecosViewSet, base_name='enderecos')
usuario_router.register('pedidos', PedidosViewSet, base_name='pedidos')

# rota de pedidos aninhada com (endereços) --> nível 3
pedidos_router = routers.NestedSimpleRouter(
    usuario_router, 'pedidos', lookup='pedido')
pedidos_router.register('enderecos', EnderecosViewSet, base_name='enderecos')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(usuario_router.urls)),
    path('api/', include(pedidos_router.urls)),
    path('admin/', admin.site.urls),
]
