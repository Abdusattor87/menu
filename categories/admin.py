from django.contrib import admin
from .models import Category
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     
    list_display=("name","category_counts")
    search_fields=("name",)

    def  category_counts(self,instance):
        return instance.categories.count()
    category_counts.short_description="Кол блюд"

 


 