from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from orders.models import Order
# Create your tests here.
class OrdersTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        #corpo da requisição de criação do pedido, encaminhando o id dos items registrados
        self.create_order = {
            "items": [1]
        }
        self.create_item = {
            "name": "caneta",
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
        
        response_create_item = self.client.post(reverse('item-list'), self.create_item, format='json')
        self.assertEqual(response_create_item.status_code, status.HTTP_201_CREATED)
        
        response_create_order = self.client.post(reverse('order-list'), self.create_order, format='json')
        self.assertEqual(response_create_order.status_code, status.HTTP_201_CREATED)
        
    def test_create_order_items(self):
        """
        CENÁRIO DE TESTE:
            Dado a rota de criação de pedido, 
            quando os dados de id dos items pedidos na requisição forem emitidos
            deve ser criado um novo pedido ao usuário autenticado 
            voltando como resposta o código (201).
        """
        response_create_order = self.client.post(reverse('order-list'), self.create_order, format='json')
        self.assertEqual(response_create_order.status_code, status.HTTP_201_CREATED)
        
    def test_list_order_user(self):
        """
        CENÁRIO DE TESTE:
            Dado a rota de listagem de pedido, 
            quando realizado requisição get na api
            deve ser listado todos os pedidos paginados
            com no máximo 10 pediodos vinculados ao usuário autenticado 
            voltando como resposta o código (200).
        """
        response_page_1 = self.client.get(reverse('order-list') + "?page=1", format='json')
        self.assertEqual(response_page_1.status_code, status.HTTP_200_OK)
        self.assertIn('next', response_page_1.data) 
        
    def test_list_details_order(self):
        """
        CENÁRIO DE TESTE:
            Dado a rota de listagem de detalhes de item do pedido, 
            quando os dados(id) na requisição forem emitidos
            deve ser listado os detalhes dos items pedidos
            pelo usuário autenticado na aplicação voltando status (200).
        """
        response_list_items_order = self.client.get(reverse('order-detail', kwargs={'pk': 1}), format='json')
        self.assertEqual(response_list_items_order.status_code, status.HTTP_200_OK)

    def test_list_notfound_items_order(self):
        """
        CENÁRIO DE TESTE:
            Dado a rota de listagem de detalhes de item do pedido, 
            quando os dados(id) na requisição forem emitidos
            caso o id do pedido fornecido não exista
            deve ser encaminhado uma exception de not found com status (404)
            para o cliente.
        """
        response_list_items_order = self.client.get(reverse('order-detail',  kwargs={'pk': 12}), format='json')
        self.assertEqual(response_list_items_order.status_code, status.HTTP_404_NOT_FOUND)