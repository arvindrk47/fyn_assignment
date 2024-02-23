from django import forms
from .models import PricingConfig, PricingTier


class PricingConfigForm(forms.ModelForm):
    class Meta:
        model = PricingConfig
        fields = ['name', 'enabled']


class PricingTierForm(forms.ModelForm):
    class Meta:
        model = PricingTier
        fields = ['day_of_week', 'distance_base_price', 'distance_upto', 'distance_additional_price', 'time_multiplier_factor_under_1h', 'time_multiplier_factor_1h_to_2h', 'time_multiplier_factor_2h_to_3h', 'waiting_charges_per_3mins']