from django.contrib.auth.models import User
from django.db import models

class PricingConfig(models.Model):
    DISTANCE_BASE_CHOICES = (
        ('Tue-Wed-Thur', 'Tue, Wed, Thur'),
        ('Sat-Mon', 'Sat, Mon'),
        ('Sun', 'Sun')
    )

    distance_base_price = models.DecimalField(max_digits=6, decimal_places=2)
    distance_additional_price = models.DecimalField(max_digits=6, decimal_places=2)
    time_multiplier_factor = models.DecimalField(max_digits=6, decimal_places=2)
    waiting_charges = models.DecimalField(max_digits=6, decimal_places=2)
    day_of_week = models.CharField(max_length=20, choices=DISTANCE_BASE_CHOICES)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_modified_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Pricing Config - {self.day_of_week}"
