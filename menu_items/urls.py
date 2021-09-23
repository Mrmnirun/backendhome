from rest_framework import routers
from .api import MenuItemViewSet

router = routers.DefaultRouter()
router.register('api/menu_items', MenuItemViewSet, 'menu_items')

urlpatterns = router.urls
