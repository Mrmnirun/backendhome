from .models import Room
from rest_framework import viewsets, permissions
from .serializers import RoomSerializer


# Room ViewSet
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomSerializer
