from items.serializers import CreateItemSerializer, ListItemsSerializer, UpdateItemSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Item
# Create your views here.
class ItemViewSet(viewsets.GenericViewSet):
    queryset = Item.objects.all()
    
    def get_serializer_class (self):
        if self.action == 'create': 
            return CreateItemSerializer
        elif self.action == 'partial_update':
            return UpdateItemSerializer
        return ListItemsSerializer
    
    def create (self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def partial_update (self, request, **kwargs):
        item = self.get_object()
        
        serializer = self.get_serializer(item, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)

    def destroy (self, request, **kwargs):
        item = self.get_object()
        
        item.delete()
        
        return Response("Item removido!",status=status.HTTP_204_NO_CONTENT)
    
    def list (self, request):
        items = self.get_queryset()
        
        serializer = self.get_serializer(items, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
