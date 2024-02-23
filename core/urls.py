from django.urls import path
from . import views

app_name = 'pricing'

urlpatterns = [
    path('', views.pricing_config, name='pricing_config'),
    path('config/', views.pricing_config_list, name='pricing_config_list'),
    path('config/create/', views.pricing_config_create, name='pricing_config_create'),
    path('config/<int:pk>/update/', views.pricing_config_update, name='pricing_config_update'),
    path('config/<int:pk>/delete/', views.pricing_config_delete, name='pricing_config_delete'),
    path('config/<int:config_pk>/tier/', views.pricing_tier_list, name='pricing_tier_list'),
    path('config/<int:config_pk>/tier/create/', views.pricing_tier_create, name='pricing_tier_create'),
    path('config/<int:config_pk>/tier/<int:pk>/update/', views.pricing_tier_update, name='pricing_tier_update'),
    path('config/<int:config_pk>/tier/<int:pk>/delete/', views.pricing_tier_delete, name='pricing_tier_delete'),
]