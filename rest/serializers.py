from .models import Furniture
from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import FurnitureDocument 

class FurnitureDocumentSerializer(DocumentSerializer):
    class Meta:
        document = FurnitureDocument
        fields = ['id', 'name', 'item_stock']

class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ['id', 'name', 'item_stock']