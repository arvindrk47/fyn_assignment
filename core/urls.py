from django.urls import path
from . import views

urlpatterns = [
    path('config/', views.pricing_config, name='pricing_config'),
    path('tier/<int:config_id>/', views.pricing_tier, name='pricing_tier'),
    path('tier/add/<int:config_id>/', views.pricing_tier, name='pricing_tier_add'),
    path('tier/edit/<int:tier_id>/', views.pricing_tier, name='pricing_tier_edit'),
]