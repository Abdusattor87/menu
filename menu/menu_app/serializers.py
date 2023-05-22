from rest_framework import serializers
from menu_app.models import Category,Product,Compound

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields =  "__all__"

class CompoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compound
        #fields =  "__all__"
        fields =("id","name")



class ProductSerializer(serializers.ModelSerializer):
  
    category = CategorySerializer()
    compound= CompoundSerializer(many=True)
      
    class Meta:
        model = Product
        fields ="__all__"



 