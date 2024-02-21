from django import forms
from .models import PricingConfig, PricingTier

class PricingConfigForm(forms.ModelForm):
    class Meta:
        model = PricingConfig
        fields = ['name', 'enabled']

class PricingTierForm(forms.ModelForm):
    class Meta:
        model = PricingTier
        fields = ['config', 'day_of_week', 'distance_upto','distance_additional_price','time_multiplier_factor','waiting_charges'] 