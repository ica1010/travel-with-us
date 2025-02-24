from rest_framework import serializers
from apps.vehicles.models import Vehicle, VehicleType
from apps.users.models import Address

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ['id', 'name', 'icon']

class VehicleSerializer(serializers.ModelSerializer):
    vehicle_type = VehicleTypeSerializer(read_only=True)
    vehicle_type_id = serializers.PrimaryKeyRelatedField(
        queryset=VehicleType.objects.all(), source='vehicle_type', write_only=True
    )
    address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())

    class Meta:
        model = Vehicle
        fields = [
            'id', 'owner', 'vehicle_type', 'vehicle_type_id', 'model', 'year', 'seats',
            'transmission', 'fuel_type', 'price_per_day', 'address', 'available_start',
            'available_end', 'description', 'is_approved', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request:
            validated_data['owner'] = request.user
        return super().create(validated_data)
