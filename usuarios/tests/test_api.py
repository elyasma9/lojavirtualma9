from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from usuarios.models import CustomUser


class UsuariosTest(APITestCase):

    def test_create_usuarios(self):
        """
        Certifique-se de que podemos criar um novo objeto de Usuarios.
        """
        url = reverse('usuarios-list')
        print(url)
        data = {
            "nome": "Inês",
            "sobrenome": "Silva",
            "email": "ines@chef.com",
            "password": "123456",
            "cpf": "07240009898",
            "rg": "34043567",
            "telefone": "79998787766",
            "is_staff": True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().nome, 'Inês')
