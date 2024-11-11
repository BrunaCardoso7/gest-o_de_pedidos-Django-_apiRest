from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from items.models import Item

class ItemsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_item = {
            "name": "caneta",
            "price": 10.0,
        }
        self.update_item = {
            "name": "caneta bic - azul",
            "price": 10.0,
        }

        self.create_user = {
            "username": "devtest",
            "email": "devtest@gmail.com",
            "password": "dev123"
        }
        self.response_create_user_test = self.client.post(reverse('user-list'), self.create_user)
        self.assertEqual(self.response_create_user_test.status_code, status.HTTP_201_CREATED)
        
        self.signin_user = {
            "username": "devtest",
            "password": "dev123"
        }
        
        self.response_signin_user_test = self.client.post(reverse('signin'), self.signin_user, format='json')
        self.assertEqual(self.response_signin_user_test.status_code, status.HTTP_200_OK)
        
        # Autenticação do usuário
        self.access_token = self.response_signin_user_test.data['tokens']['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)   

    def test_create_item_name_price(self):
        """
        CENÁRIO DE TESTE:
            Dado a rota de criação de item, 
            quando os dados na requisição forem emitidos
            deve ser criado item com dados name e price
        """
        response_create_item = self.client.post(reverse('item-list'), self.create_item, format='json')
        self.assertEqual(response_create_item.status_code, status.HTTP_201_CREATED)

    def test_update_item_name_price(self):
        """
        CENÁRIO DE TESTE:
            Dado a rota de atualização de item, 
            quando os dados na requisição forem emitidos
            deve ser atualizado dados de item como name ou price
        """
        # Cria o item
        self.client.post(reverse('item-list'), self.create_item,)

        # Atualiza o item
        response_update_item = self.client.patch(reverse('item-detail', kwargs={'pk': 1}), self.update_item,format='json')
        self.assertEqual(response_update_item.status_code, status.HTTP_206_PARTIAL_CONTENT)

    def test_delete_item(self):
        """
        CENÁRIO DE TESTE:
            Dado a rota de exclusão de item, 
            quando os dados(id) na requisição forem emitidos
            deve ser removido dados de item na aplicação.
        """
        # Cria o item
        self.client.post(reverse('item-list'), self.create_item,format='json')

        # Deleta o item
        response_delete_item = self.client.delete(reverse('item-detail', kwargs={'pk': 1}),format='json')
        self.assertEqual(response_delete_item.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_items(self):
        """
        CENÁRIO DE TESTE:
            Dado a rota de listagem de itens, 
            quando a requisição for feita
            deve retornar a lista de todos os itens cadastrados.
        """
        response_list_items = self.client.get(reverse('item-list'))
        self.assertEqual(response_list_items.status_code, status.HTTP_200_OK)
