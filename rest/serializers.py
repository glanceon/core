from .models import Furniture
from rest_framework import serializers

class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ['id', 'name', 'item_stock']