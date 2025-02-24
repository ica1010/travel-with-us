from rest_framework import viewsets, permissions
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
        """
        Les actions de création, modification et suppression nécessitent une authentification.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        """
        Pour un utilisateur non administrateur, on limite la vue aux réservations qui lui appartiennent.
        """
        user = self.request.user
        if user.is_authenticated and not user.is_staff:
            return Reservation.objects.filter(user=user)
        return Reservation.objects.all()
