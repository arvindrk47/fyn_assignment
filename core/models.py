from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PricingConfig(models.Model):
    name = models.CharField(max_length =250)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.name


class PricingTier(models.Model):
    config = models.ForeignKey(PricingConfig, on_delete = models.SET_NULL, null=True)
    day_of_week = models.IntegerField(choices=[(i,i) for i in range(7)])
    # DISTANCE BASE PRICE
    distance_upto = models.DecimalField(max_digits = 5, decimal_places = 2)
    # DAP (DISTANCE ADDITIONAL PRICE)
    distance_additional_price = models.DecimalField(max_digits = 5, decimal_places=2)
    # TMF (TIME MULTPLIER FACTOR)
    time_multiplier_factor = models.DecimalField(max_digits = 5, decimal_places = 2)
    # WC (WAITING CHARGES)
    waiting_charges = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self):
        return f"{self.config.name} - {self.day_of_week}"
    