from users.models import User
from users.serializers import CreateUserSerializer, ListUserSerializer, UpdateUserSerializer

from drf_spectacular.utils import extend_schema


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

    @extend_schema(
        tags=["Gerenciamento de usuários"],
        operation_id="user_create",
        description="Criação de um novo usuário",
        request=CreateUserSerializer,
        responses={
            201: CreateUserSerializer,
            400: "Dados inválidos"
        }
    )
    def create(self, request):  
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @extend_schema(
        tags=["Gerenciamento de usuários"],
        operation_id="user_update",
        description="Atualização de um novo usuário",
        request=UpdateUserSerializer,
        responses={
            206: UpdateUserSerializer,
            400: "Dados inválidos"
        }
    )
    def partial_update (self, request, **kwargs):
        user = self.get_object()

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)

    @extend_schema(
        tags=["Gerenciamento de usuários"],
        operation_id="user_listbyone",
        description="Atualização de um novo usuário",
        responses={
            200: ListUserSerializer,
            404: "Usuário não foi encontrado!"
        }
    )
    def retrieve (self, request, **kwargs):
        user = self.get_object()
        serializer = ListUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)