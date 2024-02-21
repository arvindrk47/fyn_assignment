from django.shortcuts import render
from .forms import PricingConfigForm, PricingTierForm
from .models import PricingConfig, PricingTier
from rest_framework import status

def pricing_config(request):
    if request.method == 'POST':
        if 'config_id' in request.POST:
            config = PricingConfig.objects.get(id=request.POST['config_id'])
            form = PricingConfigForm(request.POST, instance=config)
        else:
            form = PricingConfigForm(request.POST)
        if form.is_valid():
            config = form.save(commit=False)
            config.created_by = request.user
            config.save()
            return render(request, 'pricing/config_list.html', {'configs': PricingConfig.objects.all()})
    else:
        form = PricingConfigForm()
    return render(request, 'pricing/config_form.html', {'form': form})

def pricing_tier(request, config_id):
    config = PricingConfig.objects.get(id=config_id)
    if request.method == 'POST':
        if 'tier_id' in request.POST:
            tier = PricingTier.objects.get(id=request.POST['tier_id'])
            form = PricingTierForm(request.POST, instance=tier)
        else:
            form = PricingTierForm(request.POST)
        if form.is_valid():
            tier = form.save(commit=False)
            tier.config = config
            tier.save()
            return render(request, 'pricing/tier_list.html', {'config': config, 'tiers': PricingTier.objects.filter(config=config)})
    else:
        form = PricingTierForm()
    return render(request, 'pricing/tier_form.html', {'form': form, 'config': config})