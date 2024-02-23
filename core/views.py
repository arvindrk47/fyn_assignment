from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PricingConfig, PricingTier
from .forms import PricingConfigForm, PricingTierForm


def pricing_config_list(request):
    pricing_configs = PricingConfig.objects.all()
    return render(request, 'pricing/pricing_config_list.html', {'pricing_configs': pricing_configs})


def pricing_config_create(request):
    if request.method == 'POST':
        form = PricingConfigForm(request.POST)
        if form.is_valid():
            pricing_config = form.save(commit=False)
            pricing_config.created_by = request.user
            pricing_config.save()
            messages.success(request, 'Pricing configuration created successfully')
            return redirect('pricing_config_list')
    else:
        form = PricingConfigForm()
    return render(request, 'pricing/pricing_config_form.html', {'form': form})


def pricing_config_update(request, pk):
    pricing_config = PricingConfig.objects.get(id=pk)
    if request.method == 'POST':
        form = PricingConfigForm(request.POST, instance=pricing_config)
        if form.is_valid():
            pricing_config = form.save(commit=False)
            pricing_config.created_by = request.user
            pricing_config.save()
            messages.success(request, 'Pricing configuration updated successfully')
            return redirect('pricing_config_list')
    else:
        form = PricingConfigForm(instance=pricing_config)
    return render(request, 'pricing/pricing_config_form.html', {'form': form})


def pricing_config_delete(request, pk):
    pricing_config = PricingConfig.objects.get(id=pk)
    pricing_config.delete()
    messages.success(request, 'Pricing configuration deleted successfully')
    return redirect('pricing_config_list')


def pricing_tier_list(request, config_pk):
    pricing_config = PricingConfig.objects.get(id=config_pk)
    pricing_tiers = PricingTier.objects.filter(config=pricing_config)
    return render(request, 'pricing/pricing_tier_list.html', {'pricing_config': pricing_config, 'pricing_tiers': pricing_tiers})


def pricing_tier_create(request, config_pk):
    pricing_config = PricingConfig.objects.get(id=config_pk)
    if request.method == 'POST':
        form = PricingTierForm(request.POST)
        if form.is_valid():
            pricing_tier = form.save(commit=False)
            pricing_tier.config = pricing_config
            pricing_tier.save()
            messages.success(request, 'Pricing tier created successfully')
            return redirect('pricing_tier_list', config_pk=config_pk)
    else:
        form = PricingTierForm()
    return render(request, 'pricing/pricing_tier_form.html', {'form': form})


def pricing_tier_update(request, config_pk, pk):
    pricing_config = PricingConfig.objects.get(id=config_pk)
    pricing_tier = PricingTier.objects.get(id=pk)
    if request.method == 'POST':
        form = PricingTierForm(request.POST, instance=pricing_tier)
        if form.is_valid():
            pricing_tier = form.save(commit=False)
            pricing_tier.config = pricing_config
            pricing_tier.save()
            messages.success(request, 'Pricing tier updated successfully')
            return redirect('pricing_tier_list', config_pk=config_pk)
    else:
        form = PricingTierForm(instance=pricing_tier)
    return render(request, 'pricing/pricing_tier_form.html', {'form': form})


def pricing_tier_delete(request, config_pk, pk):
    pricing_tier = PricingTier.objects.get(id=pk)
    pricing_tier.delete()
    messages.success(request, 'Pricing tier deleted successfully')
    return redirect('pricing_tier_list', config_pk=config_pk)


def pricing_config(request):
    pricing_configs = PricingConfig.objects.all()
    return render(request, 'core/pricing_config.html', {'pricing_configs': pricing_configs})