from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Gerenciamento de pedidos API DJANGO')


router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = router.urls
