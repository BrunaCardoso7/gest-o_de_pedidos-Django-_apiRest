from django.contrib.auth import authenticate


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import extend_schema
from authentication.serializers import SigninSerializer

class SigninTokenObtainPairView(APIView):
    permission_classes = [AllowAny]
    
    @extend_schema(
        tags=["Autenticação de usuário"],
        operation_id="user_signin",
        description="Autentica um usuário usando seu nome de usuário e senha",
        request= SigninSerializer,
        responses={
            200: "retorna o token de acesso e o refresh token!",
            401: "usuário não autenticado"
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
