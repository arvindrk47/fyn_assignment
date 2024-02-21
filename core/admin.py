from django.contrib import admin
from .models import PricingConfig, PricingTier
# Register your models here.
admin.site.register(PricingConfig)
admin.site.register(PricingTier)
