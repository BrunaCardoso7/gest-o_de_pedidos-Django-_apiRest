from items.serializers import ListItemsSerializer
from rest_framework import serializers
from orders.models import Order

class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "items",
            "total",
            "create_at"
        ]
        read_only_fields = ['user']  
        
class ListOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "items",
            "total",
            "create_at"
        ]
        read_only_fields = ['user']  

class ListItemsInOrderSerializer(serializers.ModelSerializer):
    items = ListItemsSerializer(many=True)
    class Meta:
        model = Order
        fields = [
            "id",
            "items",
            "total",    
            "create_at"
        ]
        read_only_fields = ['user']  


