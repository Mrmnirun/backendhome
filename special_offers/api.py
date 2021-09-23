from .models import SpecialOffer
from rest_framework import viewsets, permissions
from .serializers import SpecialOfferSerializer


# Special Offer ViewSet
class SpecialOfferViewSet(viewsets.ModelViewSet):
    queryset = SpecialOffer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SpecialOfferSerializer
