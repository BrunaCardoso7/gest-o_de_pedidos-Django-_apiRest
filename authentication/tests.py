from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

class AuthenticateUserManagementTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user_data = {
            "username": "devtest",
            "password": "dev123"
        }

        self.user_create = {
            "username": "devtest",
            "email": "devtest@gmail.com",
            "password": "dev123"
        }

        # criar o usuário
        self.response_create_user = self.client.post(reverse('user-list'), self.user_create, format='json')
        self.assertEqual(self.response_create_user.status_code, status.HTTP_201_CREATED)

        # realizar login
        self.response_login = self.client.post(reverse('signin'), self.user_data, format='json')
        self.assertEqual(self.response_login.status_code, status.HTTP_200_OK)

        # obtendo o token de acesso
        self.access_token = self.response_login.data['tokens']['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_user_signin_account(self):
        """
        CENÁRIO DE TESTE:
            Dado a rota de signin de usuário, 
            quando os dados na requisição forem emitidos
            deve ser verificado se os campos username e  
            password são registrados na aplicação e 
            retorna o token de acesso do usuário, 
        """

        self.assertIn('access', self.response_login.data['tokens'])
        self.assertIsInstance(self.response_login.data['tokens']['access'], str)
        


    def test_user_auth_update_profile(self):
        """
        CENÁRIO DE TESTE:
            Dado a rota de de atualização de perfil do usuário, 
            quando os dados na requisição forem emitidos, 
            verifica se o usuário está autenticado e então
            deve ser atualizado campos como username ou email
            voltando como respota o status (206)
        """
        data_updated = {
            "username": "dentest_atualizado",
            "email": "devtestupdate@gmail.com"
        }
        
        response_update_profile_user = self.client.patch(reverse('user-detail', kwargs={'pk': 1}), data_updated, format='json')
        self.assertEqual(response_update_profile_user.status_code, status.HTTP_206_PARTIAL_CONTENT)



    def test_user_notauth_update_profile(self):
        """
        CENÁRIO DE TESTE:
            Dado a rota de de atualização de perfil do usuário, 
            quando os dados na requisição forem emitidos, 
            verifica se o usuário está autenticado e então
            volta como respota o status (401)
        """
        self.client.credentials()
        data_update = {
            "username": "dentest_atualizado",
        }
        response_update_profile = self.client.patch(reverse('user-detail', kwargs={'pk': 1}), data_update, format='json')
        self.assertEqual(response_update_profile.status_code, status.HTTP_401_UNAUTHORIZED)



    def test_user_auth_retriever_profile(self):
        """
        CENÁRIO DE TESTE:
            Dado a rota de de vizualização de perfil do usuário, 
            verifica se o usuário está autenticado e então
            deve ser listado os detalhes do perfil do usuário
            voltando como respota o status (200)
        """
        response_view_profile_user = self.client.get(reverse('user-detail', kwargs={'pk': 1}))
        self.assertEqual(response_view_profile_user.status_code, status.HTTP_200_OK)



    def test_user_notauth_retriever_profile(self):
        """
        CENÁRIO DE TESTE:
            Dado a rota de de vizualização de perfil do usuário, 
            verifica se o usuário está autenticado e caso não esteja,
            volta como respota o status (401)
        """
        self.client.credentials()
        response_view_profile_user = self.client.get(reverse('user-detail', kwargs={'pk': 1}))
        self.assertEqual(response_view_profile_user.status_code, status.HTTP_401_UNAUTHORIZED)
