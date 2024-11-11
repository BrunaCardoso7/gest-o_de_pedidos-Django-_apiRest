from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()

router.register(r'item', ItemViewSet, basename='item')

urlpatterns = router.urls
