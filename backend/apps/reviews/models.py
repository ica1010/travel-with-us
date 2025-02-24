# apps/reviews/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.users.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.CASCADE, null=True, blank=True)
    apartment = models.ForeignKey('apartments.Apartment', on_delete=models.CASCADE, null=True, blank=True)
    tourist_spot = models.ForeignKey('tourist_spots.TouristSpot', on_delete=models.CASCADE, null=True, blank=True)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'vehicle'],
                name='unique_vehicle_review'
            ),
            models.UniqueConstraint(
                fields=['user', 'apartment'],
                name='unique_apartment_review'
            )
        ]

    def __str__(self):
        return f"Avis de {self.user.email} - {self.rating}/5"