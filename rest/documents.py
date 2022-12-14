from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Furniture

@registry.register_document
class FurnitureDocument(Document):
    class Index:
        name = 'furniture'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Furniture
         fields = [
             'id',
             'name',
             'item_stock',
         ]