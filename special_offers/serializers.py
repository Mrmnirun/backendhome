from rest_framework import serializers
from .models import SpecialOffer

# Special Offer Serializer
class SpecialOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOffer
        fields = '__all__'