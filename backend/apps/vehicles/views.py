from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.timezone import now
from apps.vehicles.models import Vehicle, VehicleType
from apps.vehicles.serializers import VehicleSerializer, VehicleTypeSerializer

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = [permissions.AllowAny]

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        available = self.request.query_params.get('available', None)
        if available == 'true':
            queryset = queryset.filter(available_start__lte=now().date(), available_end__gte=now().date())
        return queryset

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def approve(self, request, pk=None):
        vehicle = self.get_object()
        vehicle.is_approved = True
        vehicle.save()
        return Response({'status': 'Vehicle approved'})

