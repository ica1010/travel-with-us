from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.apartments.views import ApartmentViewSet, AmenityViewSet

router = DefaultRouter()
router.register(r'apartments', ApartmentViewSet, basename='apartment')
router.register(r'amenities', AmenityViewSet, basename='amenity')

urlpatterns = [
    path('', include(router.urls)),
]
