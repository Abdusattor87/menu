from rest_framework import serializers
from menu_app.models import Product
from menu_app.serializers import *
 


class ProductSerializer(serializers.ModelSerializer):
  
    category = CategorySerializer()
    compound= CompoundSerializer(many=True)
      
    class Meta:
        model = Product
        fields ="__all__"


