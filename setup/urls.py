from authentication.views import SigninTokenObtainPairView
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
   path("signin/", SigninTokenObtainPairView.as_view(), name='signin'),
   path("api/v1/", include('users.urls')), 
   path("api/v1/", include('items.urls')), 
   path("api/v1/", include('orders.urls')), 

   # Documentação da API
   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
   path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
