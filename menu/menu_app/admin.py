from django.contrib import admin
from menu_app.models import Product,Category,Compound
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     
    list_display=("name","category_counts")
    search_fields=("name",)

    def  category_counts(self,instance):
        return instance.categories.count()
    category_counts.short_description="Кол блюд"

@admin.register(Compound)
class CompoundAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    model=Product
    list_display=("id","name","category","image","price")
    list_filter=("category",)
    search_fields=("name",)
    list_display_links=("id","name")
    list_per_page = 10
 