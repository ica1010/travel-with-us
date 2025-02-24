from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.tourist_spots.views import TouristSpotViewSet, TouristSpotCategoryViewSet

router = DefaultRouter()
router.register(r'tourist-spots', TouristSpotViewSet, basename='touristspot')
router.register(r'tourist-spot-categories', TouristSpotCategoryViewSet, basename='touristspotcategory')

urlpatterns = [
    path('', include(router.urls)),
]
