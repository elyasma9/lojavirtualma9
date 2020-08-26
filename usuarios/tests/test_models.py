from django.test import TestCase
from usuarios.models import CustomUser


class UsuarioTest(TestCase):
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

    def test_get_str(self):
        user = CustomUser.objects.get(nome="Rodrigo")
        self.assertEqual(user.__str__(), "Rodrigo Santana")
