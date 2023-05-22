from django.urls import path, include
from rest_framework import routers

from menu_app.views import ProductByCategory,MenuViewSet

router = routers.DefaultRouter()
router.register("menuinfo", MenuViewSet, "menuinfo")  



urlpatterns = [
    path('', include(router.urls)),

    path('menu/category/<int:category_id>', ProductByCategory.as_view()),
  
]