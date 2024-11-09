from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import NotFound

class CreateUserSerializer (serializers.ModelSerializer):
    class Meta :
        extra_kwargs={
            "password": {'write_only': True}
        }
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "created_at"
        ]
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)

class UpdateUserSerializer (serializers.ModelSerializer):
    class Meta :
        extra_kwargs={
            "password": {'write_only': True}
        }
        model = User
        fields = [
            "username",
            "email",
        ]


class ListUserSerializer (serializers.ModelSerializer):
    class Meta :
        model = User
        fields = [
            "id",
            "username",
            "email",
            "created_at"
        ]