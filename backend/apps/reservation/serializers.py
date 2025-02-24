from rest_framework import serializers
from .models import Reservation
from apps.vehicles.models import Vehicle
from apps.apartments.models import Apartment

class ReservationSerializer(serializers.ModelSerializer):
    # Affichage en lecture seule de l'email de l'utilisateur
    user = serializers.ReadOnlyField(source='user.email')
    # Les champs "vehicle" et "apartment" acceptent des valeurs nulles
    vehicle = serializers.PrimaryKeyRelatedField(
        queryset=Vehicle.objects.all(), allow_null=True, required=False
    )
    apartment = serializers.PrimaryKeyRelatedField(
        queryset=Apartment.objects.all(), allow_null=True, required=False
    )

    class Meta:
        model = Reservation
        fields = [
            'id', 'user', 'vehicle', 'apartment', 'start_date', 'end_date', 'total_price',
            'status', 'payment_status', 'payment_method', 'cancellation_reason',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'status', 'payment_status', 'created_at', 'updated_at']

    def validate(self, data):
        """
        Vérifie que la date de fin est postérieure à la date de début et
        qu'au moins un service (véhicule ou appartement) est renseigné.
        """
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        if start_date and end_date and end_date <= start_date:
            raise serializers.ValidationError("La date de fin doit être postérieure à la date de début.")

        if not (data.get('vehicle') or data.get('apartment')):
            raise serializers.ValidationError("La réservation doit concerner un véhicule ou un appartement.")
        return data

    def create(self, validated_data):
        """
        Associe la réservation à l'utilisateur authentifié.
        """
        request = self.context.get('request')
        if request:
            validated_data['user'] = request.user
        return super().create(validated_data)
