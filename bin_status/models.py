from django.db import models
import uuid

# Device model for API key authentication
class Device(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# BinStatus model linked to Device 
class BinStatus(models.Model):
    BIN_TYPE_CHOICES = [
        ('non-bio', 'Non-Biodegradable'),
        ('recyclable', 'Recyclable'),
    ]
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    bin_type = models.CharField(max_length=20, choices=BIN_TYPE_CHOICES)
    is_full = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.device.name}'s {self.bin_type} bin - {'Full' if self.is_full else 'Not Full'}"
