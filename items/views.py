from items.serializers import CreateItemSerializer, ListItemsSerializer, UpdateItemSerializer
from .models import Item

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.
class ItemViewSet(viewsets.GenericViewSet):
    queryset = Item.objects.all()
    
    def get_serializer_class (self):
        if self.action == 'create': 
            return CreateItemSerializer
        elif self.action == 'partial_update':
            return UpdateItemSerializer
        return ListItemsSerializer
    
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        tags=["Gerenciamento de itens"],  
        operation_description="Cria um novo item com nome e preço",
        request_body=CreateItemSerializer,
        responses={
            201: openapi.Response(
                description="Item registrado com sucesso!",
                schema=CreateItemSerializer
            ),
            400: openapi.Response(
                description="Dados inválidos"
            )
        }
    )
    def create (self, request):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(
        tags=["Gerenciamento de itens"],
        operation_description="Atualiza o nome e o preço de um item",
        request_body=UpdateItemSerializer,
        responses={
            206: openapi.Response(
                description="Atualizado com sucesso!",
                schema=UpdateItemSerializer
            ),
            404: openapi.Response(
                description="Item não encontrado!"
            )
        }
    )
    def partial_update (self, request, **kwargs):
        item = self.get_object()
        
        serializer = self.get_serializer(item, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)

    @swagger_auto_schema(
        tags=["Gerenciamento de itens"],
        operation_description="Exclue um item",
        responses={
            204: openapi.Response(
                description="Deletado com sucesso!",
            ),
            404: openapi.Response(
                description="Item não encontrado!"
            )
        }
    )
    def destroy (self, request, **kwargs):
        item = self.get_object()
        
        item.delete()
        
        return Response("Item removido!",status=status.HTTP_204_NO_CONTENT) 
    
    @swagger_auto_schema(
        tags=["Gerenciamento de itens"],
        operation_description="Recupera uma lista de todos os itens.",
        responses={
            200: openapi.Response(
                description="Listagem dos items registrados com sucesso!",
                schema=ListItemsSerializer 
            )
        }
    )   
    def list (self, request):
        items = self.get_queryset()
        
        serializer = self.get_serializer(items, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
