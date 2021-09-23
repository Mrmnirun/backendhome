from rest_framework import serializers
from .models import MenuItem

# Menu Item Serializer
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'