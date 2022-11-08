from django.urls import path
from .views import ViewFurniture, AddFurniture, UpdateFurniture, DeleteFurniture, index
urlpatterns = [
    path('view-furnitures/', ViewFurniture.as_view()),
    path('add-furniture/', AddFurniture.as_view()),
    path('update-furniture/<int:pk>', UpdateFurniture.as_view()),
    path('delete-furniture/<int:pk>', DeleteFurniture.as_view()),
    path('', index)
]