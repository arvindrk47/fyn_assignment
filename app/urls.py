
from django.urls import path
from .views import PricingConfigAPIView, CalculatePricingAPIView

urlpatterns = [
    path('pricing-config/', PricingConfigAPIView.as_view(), name='pricing-config'),
    path('calculate-pricing/', CalculatePricingAPIView.as_view(), name='calculate-pricing'),
    
]
