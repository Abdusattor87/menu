from rest_framework import serializers
from menu_app.models import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields =  "__all__"
