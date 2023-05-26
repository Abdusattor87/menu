from django.urls import path, include
from rest_framework import routers
from menu_app.views import *

router = routers.DefaultRouter()
router.register("menuinfo", MenuViewSet, "menuinfo")  
router.register("categorylist", Categorylist, "categorylist")  



urlpatterns = [
    path('', include(router.urls)),

    path('menu/category/<int:category_id>', ProductByCategory.as_view()),
  
]

 