from django.contrib import admin 
from compound.models import Compound
from django.contrib.auth.models import Group

 
@admin.register(Compound)
class CompoundAdmin(admin.ModelAdmin):

    model=Compound
    list_display=("id","name") 