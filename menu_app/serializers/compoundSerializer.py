from rest_framework import serializers
from menu_app.models import Compound

class CompoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compound
        #fields =  "__all__"
        fields =("id","name")
