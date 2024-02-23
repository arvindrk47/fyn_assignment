""" from django.test import TestCase
from .models import PricingConfig, PricingTier
from .forms import PricingConfigForm, PricingTierForm


class PricingConfigModelTests(TestCase):

   def test_pricing_config_creation(self):
       pricing_config = PricingConfig.objects.create(name='Test Config')
       self.assertTrue(pricing_config.pk)


class PricingTierModelTests(TestCase):

   def setUp(self):
       self.pricing_config = PricingConfig.objects.create(name='Test Config')

   def test_pricing_tier_creation(self):
       pricing_tier = PricingTier.objects.create(name='Test Tier', description='Test Description', price=10, config=self.pricing_config)
       self.assertTrue(pricing_tier.pk)


class PricingConfigFormTests(TestCase):

   def test_pricing_config_form_valid(self):
       form = PricingConfigForm(data={'name': 'Test Config'})
       self.assertTrue(form.is_valid())

   def test_pricing_config_form_invalid(self):
       form = PricingConfigForm(data={'name': ''})
       self.assertFalse(form.is_valid())


class PricingTierFormTests(TestCase):

   def setUp(self):
       self.pricing_config = PricingConfig.objects.create(name='Test Config')

   def test_pricing_tier_form_valid(self):
       form = PricingTierForm(data={'name': 'Test Tier', 'description': 'Test Description', 'price': 10, 'config': self.pricing_config})
       self.assertTrue(form.is_valid())

   def test_pricing_tier_form_invalid(self):
       form = PricingTierForm(data={'name': '', 'description': 'Test Description', 'price': 10, 'config': self.pricing_config})
       self.assertFalse(form.is_valid()) """