from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class SigninTokenObtainPairView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        # Adicionando prints para depuração
        print("Dados recebidos da requisição:")
        print("Username:", username)
        print("Password:", password)
        
        # Chama o authenticate e verifica a resposta
        user = authenticate(username=username, password=password)
        
        print("Resultado de authenticate:", user)  # Imprime o resultado de authenticate
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }
            }, status=status.HTTP_202_ACCEPTED)
        
        print("Autenticação falhou: credenciais incorretas")  # Mensagem para quando o usuário é None
        return Response(
            {'message': "Usuário ou senha estão incorretos!"},
            status=status.HTTP_401_UNAUTHORIZED
        )
