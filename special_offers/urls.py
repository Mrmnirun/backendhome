from rest_framework import routers
from .api import SpecialOfferViewSet

router = routers.DefaultRouter()
router.register('api/special_offers', SpecialOfferViewSet, 'special_offers')

urlpatterns = router.urls
