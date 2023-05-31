from django.contrib import admin 
from product.models import Product
from django.contrib.auth.models import Group

 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    model=Product
    list_display=("id","name","category","image","price")
    list_filter=("category",)
    search_fields=("name",)
    list_display_links=("id","name")
    list_per_page = 10
 