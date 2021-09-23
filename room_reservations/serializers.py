from rest_framework import serializers
from .models import RoomReservation


# Room Reservation Serializer
class RoomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomReservation
        fields = '__all__'
