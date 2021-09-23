from rest_framework import serializers
from .models import TableReservation


# Table Reservation Serializer
class TableReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableReservation
        fields = '__all__'
