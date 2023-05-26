
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from rest_framework.generics import ListAPIView

from menu_app.models import Product
from menu_app.serializers import ProductSerializer

class MenuViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer