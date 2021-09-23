from .models import MenuItem
from rest_framework import viewsets, permissions
from .serializers import MenuItemSerializer


# Menu Item ViewSet
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MenuItemSerializer
