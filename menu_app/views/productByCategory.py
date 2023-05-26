from rest_framework.generics import ListAPIView

from menu_app.models import Category,Product
from menu_app.serializers import ProductSerializerNoCat

 
class ProductByCategory(ListAPIView):
    serializer_class = ProductSerializerNoCat

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Product.objects.filter(category_id=category_id)
        return queryset
