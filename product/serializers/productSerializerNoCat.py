from rest_framework import serializers
from product.models import Product
from compound.serializers import CompoundSerializer
from categories.serializers import CategorySerializer
 


class ProductSerializerNoCat(serializers.ModelSerializer):

   
    compound= CompoundSerializer(many=True)
      
    class Meta:
        model = Product
        fields =("id","name","image","price","compound")


