from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.vehicles.views import VehicleViewSet, VehicleTypeViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'vehicle-types', VehicleTypeViewSet, basename='vehicletype')

urlpatterns = [
    path('', include(router.urls)),
]
