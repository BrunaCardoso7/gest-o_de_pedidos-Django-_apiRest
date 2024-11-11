from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
# Create your tests here.
class ItemsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_item = {
            "name": "caneta",
            "price": 10.0,
        }
        self.update_item= {
            "name": "caneta bic - azul",
            "price": 10.0,
        }
        
        self.create_user = {
            "username": "devtest",
            "email": "devtest@gmail.com",
            "password": "dev123"
        }
        self.response_create_user_test = self.client.post('user-list', self.create_user)
        self.assertEqual(self.response_create_user_test.status_code, status.HTTP_201_CREATED)
        
        self.signin_user = {
            "username": "devtest",
            "password": "dev123"
        }
        
        self.response_signin_user_test = self.client.post('signin', self.signin_user, format='json')
        self.assertEqual(self.response_signin_user_test.status_code, status.HTTP_200_OK)
        
    def test_create_item_name_price(self):
        """"
        CENÁRIO DE TESTE:
            Dado a rota de criação de item, 
            quando os dados na requisição forem emitidos
            deve ser criado item com dados name e price
        """
        response_create_item_name_price = self.client.post('item-list', self.create_item)
        self.assertEquals(response_create_item_name_price.status_code, status.HTTP_201_CREATED)

    def test_update_item_name_price(self):
        """"
        CENÁRIO DE TESTE:
            Dado a rota de atualização de item, 
            quando os dados na requisição forem emitidos
            deve ser atualizado dados de item como name ou price
        """
        response_update_item_name_price = self.client.patch('item-detail', self.update_item)
        self.assertEquals(response_update_item_name_price.status_code, status.HTTP_206_PARTIAL_CONTENT)

    def test_delete_item(self):
        """"
        CENÁRIO DE TESTE:
            Dado a rota de atualização de item, 
            quando os dados(id) na requisição forem emitidos
            deve ser removido dados de item na aplicação,
        """
        response_delete_item = self.client.delete('item-detail')
        self.assertEquals(response_delete_item.status_code, status.HTTP_204_NO_CONTENT)