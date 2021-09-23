from rest_framework import routers
from .api import RoomViewSet

router = routers.DefaultRouter()
router.register('api/rooms', RoomViewSet, 'rooms')

urlpatterns = router.urls
