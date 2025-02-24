# apps/vehicles/models.py
from django.db import models
from apps.users.models import User
from apps.users.models import Address

class VehicleType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.PROTECT)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    seats = models.PositiveIntegerField()
    transmission = models.CharField(max_length=20, choices=[('manual', 'Manuelle'), ('auto', 'Automatique')])
    fuel_type = models.CharField(max_length=20, choices=[('essence', 'Essence'), ('diesel', 'Diesel'), ('elec', 'Électrique')])
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    available_start = models.DateField()
    available_end = models.DateField()
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['price_per_day']),
            models.Index(fields=['available_start', 'available_end']),
        ]

    def __str__(self):
        return f"{self.model} ({self.vehicle_type})"