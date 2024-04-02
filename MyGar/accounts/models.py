from django.db import models
from django.conf import settings

class Car(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars')
    vin = models.CharField(max_length=50, unique=True)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.brand} {self.model} (VIN: {self.vin})"
