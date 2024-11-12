from django.contrib.auth import authenticate


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class SigninTokenObtainPairView(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        tags=["Autenticação de usuário"],
        operation_description="Autentica um usuário usando seu nome de usuário e senha",
        responses={
            200: openapi.Response(
                description="Usuário autenticado com sucesso!",
            )
        }
    )   
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }
            }, status=status.HTTP_200_OK)
        
        return Response(
            {'message': "Usuário ou senha estão incorretos!"},
            status=status.HTTP_401_UNAUTHORIZED
        )
