from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from produtos.models import Produto


class ProdutoTests(APITestCase):
    def test_create_produto(self):
        """
        Certifique-se de que podemos criar um novo objeto de Produto.
        """
        url = reverse("produtos-list")
        data = {"nome": "arroz", "preco": "2.30"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.count(), 1)
        self.assertEqual(Produto.objects.get().nome, "arroz")

    def test_list_produto(self):
        """
        Certifique-se de que podemos todos os objetos de Produto.
        """
        url = reverse("produtos-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Produto.objects.get(), response)
