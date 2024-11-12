from items.serializers import CreateItemSerializer, ListItemsSerializer, UpdateItemSerializer
from .models import Item

from drf_spectacular.utils import extend_schema

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
    
    @extend_schema(
        tags=["Gerenciamento de itens"],
        operation_id="item_create",
        description="Atualização de um novo item",
        request=CreateItemSerializer,
        responses={
            201: CreateItemSerializer,
            400: "Dados inválidos"
        }
    )
    def create (self, request):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @extend_schema(
        tags=["Gerenciamento de itens"],
        operation_id="item_update",
        description="Atualização de um item",
        request=UpdateItemSerializer,
        responses={
            206: UpdateItemSerializer,
            400: "Dados inválidos"
        }
    )
    def partial_update (self, request, **kwargs):
        item = self.get_object()
        
        serializer = self.get_serializer(item, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)

    @extend_schema(
        tags=["Gerenciamento de itens"],
        operation_id="item_delete",
        description="Remoção de um item",
        responses={
            204: "item removido com sucesso",
            400: "Dados inválidos"
        }
    )
    def destroy (self, request, **kwargs):
        item = self.get_object()
        
        item.delete()
        
        return Response("Item removido!",status=status.HTTP_204_NO_CONTENT) 
    
    @extend_schema(
        tags=["Gerenciamento de itens"],
        operation_id="item_listall",
        description="lista todos os item registrados",
        responses={
            200: ListItemsSerializer,
        }
    )
    def list (self, request):
        items = self.get_queryset()
        
        serializer = self.get_serializer(items, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
