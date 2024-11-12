from users.models import User
from users.serializers import CreateUserSerializer, ListUserSerializer, UpdateUserSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated, AllowAny

class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        elif self.action == 'partial_update':
            return UpdateUserSerializer
        return ListUserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    @swagger_auto_schema(
        tags=["Gerenciamento de usuários"],
        operation_description="Criação de um novo usuário",
        request_body=CreateUserSerializer,
        responses={
            201: openapi.Response(
                description="Registrado com sucesso!",
                schema=CreateUserSerializer
            ),
            400: openapi.Response(
                description="Dados inválidos"
            )
        }
    )
    def create(self, request):  
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(
        tags=["Gerenciamento de usuários"],
        operation_description="Atualização do perfil do usuário",
        request_body=UpdateUserSerializer,
        responses={
            206: openapi.Response(
                description="Atualizado com sucesso!",
                schema=UpdateUserSerializer
            ),
            404: openapi.Response(
                description="Usuário não encontrado!"
            )
        }
    )
    def partial_update (self, request, **kwargs):
        user = self.get_object()

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
    
    @swagger_auto_schema(
        tags=["Gerenciamento de usuários"],  
        operation_description="Detalhes do perfil do usuário",
        responses={
            200: openapi.Response(
                description="Detalhes de usuários com sucesso!",
                schema=ListUserSerializer
            ),
            404: openapi.Response(
                description="Usuário não encontrado!"
            )
        }
    )
    def retrieve (self, request, **kwargs):
        user = self.get_object()
        serializer = ListUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)