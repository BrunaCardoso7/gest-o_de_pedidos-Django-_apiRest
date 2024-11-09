from rest_framework import serializers
from users.models import User

class UserSerializer (serializers.ModelSerializer):
    class Meta :
        extra_kwargs={
            "password": {'write_only': True}
        }
        model = User
        fields = {
            "id",
            "username",
            "email",
            "created_at"
        }