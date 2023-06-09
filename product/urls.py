from django.urls import path, include
from rest_framework import routers 
from product.views import MenuViewSet,ProductByCategory

router = routers.DefaultRouter()   
router.register("", MenuViewSet, "menuinfo")   
 
 
urlpatterns = [
    path('', include(router.urls)),
    path('category/<int:category_id>', ProductByCategory.as_view()),
] 