from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class BinStatus(models.Model):
    bio_status = models.CharField(max_length=20, default="empty") 
    recyclable_status = models.CharField(max_length=20, default="empty")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bio: {self.bio_status}, Recyclable: {self.recyclable_status} (updated {self.updated_at})"
