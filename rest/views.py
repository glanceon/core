from rest_framework.views import APIView

# Token Auth
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# Cache Decorators
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

# Response
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import HttpResponse

# Document Viewset
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet

# Document Filter
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend

# Custom Models/Serializers
from .models import Furniture
from .serializers import FurnitureSerializer, FurnitureDocumentSerializer
from .documents import FurnitureDocument

# Celery Tasks
from .tasks import CustomTask


# Views begin here.
# /api/
# Worker does CustomTask function on background server
def index(request):
    CustomTask.delay()
    return HttpResponse("Done")

# Generate Token
# [POST] /api-token-auth/
# [Body] "username" "password"
# Response JSON
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

# [GET] /api/view-furnitures/ 
# !!cache set for 1 hour
# show list of furnitures.. I'm not creative enough
# Response JSON
class ViewFurniture(BaseDocumentViewSet):
    document = FurnitureDocument
    serializer_class = FurnitureDocumentSerializer
    filter_backends = [SearchFilterBackend]

    search_fields = [
        'id',
        'name',
        'item_stock'
    ]

# [POST] [AUTH] /api/add-furniture/
# Auth example - [Header] "Authorization":"token 14a9fc6ce6fb99a3bfd195013a036bf5fca85478"
# [Body] "char:name" "int:item_stock"
# Response 201 CREATED | 400 BAD_REQUEST
class AddFurniture(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = FurnitureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# [POST] [AUTH] /api/update-furniture/<int:pk>
# Auth example - [Header] "Authorization":"token 14a9fc6ce6fb99a3bfd195013a036bf5fca85478"
# [Body] "char:name" "int:item_stock"
# Response 200 OK | 400 BAD_REQUEST
class UpdateFurniture(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, pk, format=None, *args, **kwargs):
        furniture = Furniture.objects.get(id=pk)
        serializer = FurnitureSerializer(instance=furniture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# [DELETE] [AUTH] api/delete-furniture/<int:pk>
# Auth example - [Header] "Authorization":"token 14a9fc6ce6fb99a3bfd195013a036bf5fca85478"
# [Body] "char:name" "int:item_stock"
# Response 200 OK | 400 BAD_REQUEST
class DeleteFurniture(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk, format=None):
        try:
            furniture = Furniture.objects.get(id=pk)
            furniture.delete()
        except:
            return Response(status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)