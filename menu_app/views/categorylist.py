from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

 

from menu_app.models import Category
from menu_app.serializers import  CategorySerializer

 
class Categorylist(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class =  CategorySerializer