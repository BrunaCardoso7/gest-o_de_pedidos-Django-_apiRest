from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
# Create your tests here.
class UserMagnamentTest (TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "username": "devtest",
            "email": "devtest@gmail.com",
            "password": "dev123"
        }

    def test_create_user_username_email_unique(self):
        """"
        CENÁRIO DE TESTE:
            Dado a rota de criação de usuário, 
            quando os dados na requisição forem emitidos
            deve ser verificado se os campos username e email
            são exclusivos e só então cadastrar o usuário
        """
        response = self.client.post(reverse('user-list'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response_duplicate = self.client.post(reverse('user-list'), self.user_data)
        self.assertEqual(response_duplicate.status_code, status.HTTP_400_BAD_REQUEST)
        
        self.assertIn("username", response_duplicate.data)
        self.assertIn("email", response_duplicate.data)
