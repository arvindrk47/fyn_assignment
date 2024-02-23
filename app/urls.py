
from django.urls import path
from .views import PricingConfigAPIView, CalculatePricingAPIView, LoggerInfoAPIView

urlpatterns = [
    path('pricing-config/', PricingConfigAPIView.as_view(), name='pricing-config'),
    path('calculate-pricing/', CalculatePricingAPIView.as_view(), name='calculate-pricing'),
    path('logger-info/', LoggerInfoAPIView.as_view(), name='logger-info'),   
]
