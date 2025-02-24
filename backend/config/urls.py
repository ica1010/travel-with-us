from django.contrib import admin
from django.urls import include, path
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from apps.vehicles.views import VehicleViewSet
from apps.apartments.views import ApartmentViewSet
from apps.tourist_spots.views import TouristSpotViewSet
from apps.reviews.views import ReviewViewSet
from apps.reservation.views import ReservationViewSet

# Définir le router
router = DefaultRouter()

# Enregistrer les viewsets
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'apartments', ApartmentViewSet, basename='apartment')
router.register(r'tourist-spots', TouristSpotViewSet, basename='tourist-spot')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'reservations', ReservationViewSet, basename='reservation')

# Fonction API Root
def api_root(request):
    return JsonResponse({
        "message": "Bienvenue sur notre API. Vous pouvez explorer les endpoints via /api/."
    })

# Définir les URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.users.urls')),
    path('api/', include(router.urls)),  # Utiliser le router pour les endpoints de l'API
    path('', api_root, name='api-root'),
]
