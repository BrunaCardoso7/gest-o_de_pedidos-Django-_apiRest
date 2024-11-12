from orders.serializers import (CreateOrderSerializer, ListItemsInOrderSerializer,
    ListOrderSerializer)
from orders.models import Order
from items.models import Item

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, OpenApiResponse
from drf_spectacular.openapi import OpenApiTypes

from rest_framework.pagination import PageNumberPagination

class OrderViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action =='create':
            return CreateOrderSerializer
        elif self.action == 'retrieve':
            return ListItemsInOrderSerializer
        return ListOrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


    @extend_schema(
        tags=["Gestão de Pedidos"],
        operation_id="order_create",
        description="Criação de um novo usuário",
        request=CreateOrderSerializer,
        responses={
            201: CreateOrderSerializer,
            400: "Dados inválidos"
        }
    )
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            items_ids = request.data.get('items', [])
            
            items = Item.objects.filter(id__in=items_ids)
            total = sum(item.price for item in items)
            
            order = serializer.save(user=request.user)
            order.total = total
            order.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    @extend_schema(
        tags=["Gestão de Pedidos"],
        operation_id="order_listall",
        description="Listagem de todos os pedidos do usuário",
        responses={
            200: OpenApiResponse(
                description="Lista de pedidos do usuário",
                response=OpenApiTypes.OBJECT,
            ),
        },
    )
    def list(self, request):
        queryset = Order.objects.all()
        
        paginator = PageNumberPagination()
        paginator.page_size = 10  
        paginate_orders = paginator.paginate_queryset(queryset, request)
        
        serializer = ListOrderSerializer(paginate_orders, many=True)
        
        return paginator.get_paginated_response(serializer.data)
    

    @extend_schema(
        tags=["Gestão de Pedidos"],
        operation_id="order_findbyone",
        description="Listagem de detalhes do pedido",
        responses={
            201: ListItemsInOrderSerializer,
            400: "Dados inválidos"
        }
    )
    def retrieve(self, request, pk=None):
        try:
            order = self.get_queryset().get(pk=pk)
        except Order.DoesNotExist:
            return Response("Pedido não entrado!", status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
