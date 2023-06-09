from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from categories.models import Category
from categories.serializers import  CategorySerializer

 
class CategoryViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class =  CategorySerializer