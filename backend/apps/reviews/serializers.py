from rest_framework import serializers
from apps.reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    # Affichage en lecture seule de l'email de l'utilisateur
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Review
        fields = [
            'id', 'user', 'vehicle', 'apartment', 'tourist_spot', 'rating', 'comment',
            'is_approved', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'is_approved', 'created_at', 'updated_at']

    def validate(self, data):
        """
        Vérifie qu'au moins l'un des champs 'vehicle', 'apartment' ou 'tourist_spot'
        est renseigné, car l'avis doit concerner un type de service.
        """
        if not (data.get('vehicle') or data.get('apartment') or data.get('tourist_spot')):
            raise serializers.ValidationError(
                "L'avis doit être associé à un véhicule, un appartement ou un lieu touristique."
            )
        return data

    def create(self, validated_data):
        """
        Associe l'avis à l'utilisateur authentifié lors de la création.
        """
        request = self.context.get('request')
        if request:
            validated_data['user'] = request.user
        return super().create(validated_data)
