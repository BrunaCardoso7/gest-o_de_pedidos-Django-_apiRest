from django.contrib import admin
from django.urls import path, include
from authentication.views import SigninTokenObtainPairView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Configuração do Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Gerenciamento de Pedidos API",
      default_version='v1',
      description="Documentação completa de todas as APIs do projeto",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@dominio.com"),
      license=openapi.License(name="Licença MIT"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path("admin/", admin.site.urls),
   path("signin/", SigninTokenObtainPairView.as_view(), name='signin'),
   path("api/v1/", include('users.urls')), 
   path("api/v1/", include('items.urls')), 
   path("api/v1/", include('orders.urls')), 
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
]
