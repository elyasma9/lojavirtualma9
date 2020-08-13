from django.test import TestCase
from produtos.models import Produto


class ProdutoTestCase(TestCase):

    def setUp(self):
        Produto.objects.create(
            nome='arroz',
            preco=2.30
        )

    def test_get_str(self):
        produto = Produto.objects.get(nome='arroz')
        self.assertEquals(produto.__str__(), 'arroz')
