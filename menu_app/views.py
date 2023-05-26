from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny

from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.generics import ListAPIView

from menu_app.models import Category,Product
from menu_app.serializers import ProductSerializer, CategorySerializer

class MenuViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Categorylist(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class =  CategorySerializer

class ProductByCategory(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Product.objects.filter(category_id=category_id)
        return queryset
