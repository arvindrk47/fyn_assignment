from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from decimal import Decimal
from .models import PricingConfig

class PricingConfigAPITestCase(TestCase):
    def setUp(self):
        self.pricing_config_url = reverse('pricing-config')
        self.calculate_pricing_url = reverse('calculate-pricing')

    def test_create_pricing_config(self):
        data = {
            'distance_base_price': '80.0',
            'distance_additional_price': '30.0',
            'time_multiplier_factor': '1.0',
            'waiting_charges': '5.0',
            'day_of_week': 'Tue-Wed-Thur',
            'active': 'True',
        }

        response = self.client.post(self.pricing_config_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        
    def test_calculate_pricing(self):
        # Create a PricingConfig instance for testing
        PricingConfig.objects.create(
            distance_base_price=80.0,
            distance_additional_price=30.0,
            time_multiplier_factor=1.0,
            waiting_charges=5.0,
            day_of_week='Tue-Wed-Thur',
            active=True
        )

        # Prepare data for the CalculatePricingAPIView
        data = {
            'distance': 10.0,
            'time': 2.0,
            'waiting_duration': 1.0,
            'day_of_week': 'Tue-Wed-Thur',
        }

        # Make a POST request to the CalculatePricingAPIView
        response = self.client.post(self.calculate_pricing_url, data)

        # Check if the response has a 'price' key in the JSON content
        self.assertIn('price', response.json())