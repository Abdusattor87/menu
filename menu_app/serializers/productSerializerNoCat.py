from rest_framework import serializers
from menu_app.models import Product
from menu_app.serializers import *
 


class ProductSerializerNoCat(serializers.ModelSerializer):
   
    compound= CompoundSerializer(many=True)
      
    class Meta:
        model = Product
        fields =("id","name","image","price","compound",)


