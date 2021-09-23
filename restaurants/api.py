from .models import Restaurant
from rest_framework import viewsets, permissions
from .serializers import RestaurantSerializer


# Restaurant ViewSet
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RestaurantSerializer
