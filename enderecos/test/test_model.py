from django.test import TestCase
from usuarios.models import CustomUser
from enderecos.models import Endereco


class EnderecoTest(TestCase):

    def setUp(self):

        user = CustomUser.objects.create(
            nome='Rodrigo',
            sobrenome='Santana',
            email='rodsantana@gmail.com',
            password='mary1kim2',
            cpf='07888889877',
            rg='98976540',
            is_staff=True,
            is_active=True)

        endereco = Endereco.objects.create(
            logradouro='Rua dois Loteamento Carajás',
            bairro='Bairro Marcos Freire 2/Taiçoca',
            cep='49160-000',
            cidade='NOSSA SENHORA DO SOCORRO',
            estado='SE',
            numero='78',
            user=user)

    def test_get_str(self):
        endereco = Endereco.objects.get(cidade='NOSSA SENHORA DO SOCORRO')
        self.assertEquals(endereco.__str__(
        ), 'NOSSA SENHORA DO SOCORRO, Rua dois Loteamento Carajás')
