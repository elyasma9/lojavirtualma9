from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from enderecos.models import Endereco
from usuarios.models import CustomUser


class EnderecosTest(APITestCase):

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

    def test_create_enderecos(self):
        """
        Certifique-se de que podemos criar um novo objeto de endereços.
        """
        url = reverse('enderecos-list', args=['1'])
        data = {
            "logradouro": "Rua dois Loteamento Carajás",
            "bairro": "Bairro Marcos Freire 2/Taiçoca",
            "cep": "49160-000",
            "cidade": "NOSSA SENHORA DO SOCORRO",
            "estado": "SE",
            "numero": "78",
            "user": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Endereco.objects.get().user.id, 1)
