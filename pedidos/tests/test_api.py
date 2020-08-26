from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from usuarios.models import CustomUser
from produtos.models import Produto
from enderecos.models import Endereco
from pedidos.models import Pedido


class PedidosTest(APITestCase):
    def setUp(self):

        user = CustomUser.objects.create(
            nome="Rodrigo",
            sobrenome="Santana",
            email="rodsantana@gmail.com",
            password="mary1kim2",
            cpf="07888889877",
            rg="98976540",
            is_staff=True,
            is_active=True,
        )

        produto = Produto.objects.create(nome="arroz", preco=2.30)

        endereco = Endereco.objects.create(
            logradouro="Rua dois Loteamento Carajás",
            bairro="Bairro Marcos Freire 2/Taiçoca",
            cep="49160-000",
            cidade="NOSSA SENHORA DO SOCORRO",
            estado="SE",
            numero="78",
            user=user,
        )

    def test_create_pedidos(self):
        """
        Certifique-se de que podemos criar um novo objeto de pedidos.
        """
        url = reverse("pedidos-list", args=["1"])
        print(url)
        data = {
            "user": 1,
            "produtos": [1],
            "status": "P",
            "endereco": 1,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pedido.objects.count(), 1)
        self.assertEqual(Pedido.objects.get().status, "P")
