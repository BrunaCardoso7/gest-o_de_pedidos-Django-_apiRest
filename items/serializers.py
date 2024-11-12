from rest_framework import serializers
from .models import Item

class CreateItemSerializer (serializers.ModelSerializer):
    class Meta :
        model = Item
        fields = [
            "id",
            "name",
            "price",
            "created_at"
        ]
        
class ListItemsSerializer (serializers.ModelSerializer):
    class Meta :
        model = Item
        fields = [
            "id",
            "name",
            "price",
            "created_at"
        ]

class UpdateItemSerializer (serializers.ModelSerializer):
    class Meta :
        model = Item
        fields = [
            "id",
            "name",
            "price",
            "created_at"
        ]