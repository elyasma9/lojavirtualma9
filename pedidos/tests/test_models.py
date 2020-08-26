from django.test import TestCase
from pedidos.models import Pedido
from usuarios.models import CustomUser
from produtos.models import Produto
from enderecos.models import Endereco


class PedidosTest(TestCase):
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
        user.save()

        produtos = Produto.objects.create(nome="arroz", preco=2.30)
        produtos.save()

        endereco = Endereco.objects.create(
            logradouro="Rua dois Loteamento Carajás",
            bairro="Bairro Marcos Freire 2/Taiçoca",
            cep="49160-000",
            cidade="NOSSA SENHORA DO SOCORRO",
            estado="SE",
            numero="78",
            user=user,
        )
        endereco.save()

        pedidos = Pedido.objects.create(
            user=user,
            status="P",
            endereco=endereco,
        )

        pedidos.produtos.add(produtos)

    def test_get_str(self):
        pedido = Pedido.objects.get(status="P")
        self.assertEqual(
            pedido.__str__(),
            "Rodrigo Santana, esse é o seu carrinho.",
        )
