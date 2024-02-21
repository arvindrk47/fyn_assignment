from django.shortcuts import render
from .forms import PricingConfigForm, PricingTierForm
from .models import PricingConfig, PricingTier
from rest_framework import status
# Create your views here.

def pricing_config(request):
    if request.method == 'POST':
        if 'config_id' in request.POST:
            config = PricingConfig.objects.get(id=request.POST['config_id'])
            form = PricingConfigForm(request.POST, instance = config)
        else:
            form = PricingConfigForm(request.POST)
        

        if form.is_valid():
            config = form.save(commit = False)
            config.created_by = request.user
            config.save()
            return status(status = status.HTTP_201_CREATED)
        