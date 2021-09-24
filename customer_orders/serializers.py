from rest_framework import serializers
from .models import CustomerOrder


# Customer Order Serializer
class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = '__all__'
