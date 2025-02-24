from rest_framework import viewsets, permissions
from apps.tourist_spots.models import TouristSpot, TouristSpotCategory
from apps.tourist_spots.serializers import TouristSpotSerializer, TouristSpotCategorySerializer

class TouristSpotCategoryViewSet(viewsets.ModelViewSet):
    queryset = TouristSpotCategory.objects.all()
    serializer_class = TouristSpotCategorySerializer
    permission_classes = [permissions.AllowAny]

class TouristSpotViewSet(viewsets.ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer

    def get_permissions(self):
        # Seules les actions de création et modification nécessitent l'authentification
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        queryset = TouristSpot.objects.all()
        # Filtrage optionnel sur les spots en vedette via ?featured=true
        featured = self.request.query_params.get('featured', None)
        if featured == 'true':
            queryset = queryset.filter(is_featured=True)
        return queryset
