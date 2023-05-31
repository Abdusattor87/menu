from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView


from product.models import Product
from product.serializers import ProductSerializerNoCat,ProductSerializer

 
class ProductByCategory(ListAPIView):
    serializer_class = ProductSerializerNoCat

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Product.objects.filter(category_id=category_id)
        return queryset


class MenuViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer