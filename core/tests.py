from django.test import TestCase
from django.contrib.auth.models import User
from .models import PricingConfig, PricingTier
from .forms import PricingConfigForm, PricingTierForm
from .pricing import evaluate_price
# Create your tests here.
class PricingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.config = PricingConfig.objects.create(name='Test Config', created_by=self.user)
        self.tier = PricingTier.objects.create(config=self.config, day_of_week=1, distance_upto=10, distance_additional_price=1.5, time_multiplier_factor=2.0, waiting_charges=0.5)

    def test_pricing_config_created(self):
        config = PricingConfig.objects.create(name='Test Config', created_by=self.user)
        self.assertTrue(config.pk)

    def test_pricing_tier_created(self):
        tier = PricingTier.objects.create(config=self.config, day_of_week=1, distance_upto=10, distance_additional_price=1.5, time_multiplier_factor=2.0, waiting_charges=0.5)
        self.assertTrue(tier.pk)

    def test_pricing_config_form_valid(self):
        form = PricingConfigForm(data={'name': 'Test Config', 'enabled': True})
        self.assertTrue(form.is_valid())

    def test_pricing_config_form_invalid(self):
        form = PricingConfigForm(data={'name': '', 'enabled': True})
        self.assertFalse(form.is_valid())

    def test_pricing_tier_form_valid(self):
        form = PricingTierForm(data={'config': self.config.pk, 'day_of_week': 1, 'distance_upto': 10, 'distance_additional_price': 1.5, 'time_multiplier_factor': 2.0, 'waiting_charges': 0.5})
        self.assertTrue(form.is_valid())

    def test_pricing_tier_form_invalid(self):
        form = PricingTierForm(data={'config': self.config.pk, 'day_of_week': '', 'distance_upto': 10, 'distance_additional_price': 1.5, 'time_multiplier_factor': 2.0, 'waiting_charges': 0.5})
        self.assertFalse(form.is_valid())

    def test_pricing_evaluation(self):
        distance = 15
        time = 30
        price = evaluate_price(self.config, distance, time)
        self.assertEqual(price, 52.5)