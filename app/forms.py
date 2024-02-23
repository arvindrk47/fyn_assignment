from django import forms
from django.utils import timezone
from .models import PricingConfig
import logging

# Configure logger
logger = logging.getLogger(__name__)

class PricingConfigForm(forms.ModelForm):
    class Meta:
        model = PricingConfig
        fields = '__all__'

    def save(self, commit=True, user=None):
        # Save the user who is making the change and timestamp
        instance = super().save(commit=False)
        
        # Set the user and timestamp
        instance.last_modified_by = user
        instance.last_modified_at = timezone.now()

        if commit:
            instance.save()

            # Log the configuration change
            logger.info(f"Pricing configuration modified by {user} at {instance.last_modified_at}")

        return instance
