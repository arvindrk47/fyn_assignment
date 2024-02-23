from django.db import models
from django.contrib.auth.models import User



class PricingConfig(models.Model):
    name = models.CharField(max_length=250)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class PricingTier(models.Model):
    config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=[(i, i) for i in range(7)])
    distance_base_price = models.DecimalField(max_digits=5, decimal_places=2)
    distance_upto = models.DecimalField(max_digits=5, decimal_places=2)
    distance_additional_price = models.DecimalField(max_digits=5, decimal_places=2)
    time_multiplier_factor_under_1h = models.DecimalField(max_digits=5, decimal_places=2)
    time_multiplier_factor_1h_to_2h = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    time_multiplier_factor_2h_to_3h = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    waiting_charges_per_3mins = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.config.name} - {self.day_of_week}"