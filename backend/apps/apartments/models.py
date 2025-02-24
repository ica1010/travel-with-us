# apps/apartments/models.py
from django.db import models
from apps.users.models import User
from apps.users.models import Address

class Amenity(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Amenities"

    def __str__(self):
        return self.name

class Apartment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apartments')
    title = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    max_guests = models.PositiveIntegerField()
    amenities = models.ManyToManyField(Amenity)
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    cancellation_policy = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['price_per_night']),
        ]

    def __str__(self):
        return f"{self.title} - {self.address.city}"