from rest_framework import serializers
from apps.apartments.models import Apartment, Amenity

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'name', 'category']

class ApartmentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    # Pour l'affichage, on utilise le sérialiseur de l'amenity
    amenities = AmenitySerializer(many=True, read_only=True)
    # Pour la création/mise à jour, on passe une liste d'IDs
    amenities_ids = serializers.PrimaryKeyRelatedField(
        queryset=Amenity.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Apartment
        fields = [
            'id', 'owner', 'title', 'address', 'price_per_night', 'bedrooms',
            'bathrooms', 'max_guests', 'amenities', 'amenities_ids', 'check_in_time',
            'check_out_time', 'cancellation_policy', 'is_approved', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'owner', 'is_approved', 'created_at', 'updated_at']

    def create(self, validated_data):
        amenities_data = validated_data.pop('amenities_ids', [])
        request = self.context.get('request')
        if request:
            validated_data['owner'] = request.user
        apartment = Apartment.objects.create(**validated_data)
        if amenities_data:
            apartment.amenities.set(amenities_data)
        return apartment

    def update(self, instance, validated_data):
        amenities_data = validated_data.pop('amenities_ids', None)
        instance = super().update(instance, validated_data)
        if amenities_data is not None:
            instance.amenities.set(amenities_data)
        return instance
