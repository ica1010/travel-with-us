from rest_framework import serializers
from apps.tourist_spots.models import TouristSpot, TouristSpotCategory
from apps.users.models import Address

class TouristSpotCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristSpotCategory
        fields = ['id', 'name', 'icon']

class TouristSpotSerializer(serializers.ModelSerializer):
    # Affichage en lecture seule de la catégorie
    category = TouristSpotCategorySerializer(read_only=True)
    # Pour la création/modification, on passe l'ID de la catégorie
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=TouristSpotCategory.objects.all(), source='category', write_only=True
    )
    address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())

    class Meta:
        model = TouristSpot
        fields = [
            'id', 'name', 'category', 'category_id', 'address', 'description',
            'opening_hours', 'entrance_fee', 'website', 'popularity_score',
            'is_featured', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'popularity_score', 'created_at', 'updated_at']
