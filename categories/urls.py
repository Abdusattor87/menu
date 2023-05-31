from django.urls import path, include
from rest_framework import routers
from categories.views import Categorylist 

router = routers.DefaultRouter()  
router.register("categorylist", Categorylist, "categorylist")  



urlpatterns = [
    path('', include(router.urls)), 
] 