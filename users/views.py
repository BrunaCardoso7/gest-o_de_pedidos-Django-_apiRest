from users.models import User
from users.serializers import CreateUserSerializer, ListUserSerializer, UpdateUserSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response

class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        elif self.action == 'partial_update':
            return UpdateUserSerializer
        return ListUserSerializer

    def create(self, request):
        print("Dados recebidos no registro:", request.data)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def partial_update (self, request, **kwargs):
        user = self.get_object()

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
    
    def retrieve (self, request, **kwargs):
        user = self.get_object()
        serializer = ListUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)