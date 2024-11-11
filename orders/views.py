from orders.serializers import (CreateOrderSerializer, ListItemsInOrderSerializer,
    ListOrderSerializer)
from rest_framework.permissions import IsAuthenticated
from orders.models import Order
from rest_framework import viewsets, status
from rest_framework.response import Response

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

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        try:
            order = self.get_queryset().get(pk=pk)
        except Order.DoesNotExist:
            return Response("Pedido não entrado!", status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(order)
        return Response(serializer.data)
