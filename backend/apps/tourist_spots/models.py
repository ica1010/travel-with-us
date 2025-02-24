# apps/tourist_spots/models.py
from django.db import models
from apps.users.models import Address

class TouristSpotCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Tourist spot categories"

    def __str__(self):
        return self.name

class TouristSpot(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(TouristSpotCategory, on_delete=models.PROTECT)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    description = models.TextField()
    opening_hours = models.TextField()
    entrance_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    website = models.URLField(blank=True)
    popularity_score = models.FloatField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-popularity_score']
        indexes = [
            models.Index(fields=['popularity_score']),
        ]

    def __str__(self):
        return self.name