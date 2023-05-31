from rest_framework import serializers
from product.models import Product
from compound.serializers import CompoundSerializer
from categories.serializers import CategorySerializer
 


class ProductSerializer(serializers.ModelSerializer):
  
    category = CategorySerializer()
    compound= CompoundSerializer(many=True)
      
    class Meta:
        model = Product
        fields ="__all__"


