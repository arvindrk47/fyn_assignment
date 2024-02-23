import logging
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PricingConfig
from .forms import PricingConfigForm
from .serializers import PricingConfigSerializer
from decimal import Decimal
from rest_framework import status

# Configure logger
logger = logging.getLogger(__name__)

class PricingConfigAPIView(APIView):
    def get(self, request):
        # Fetch all pricing configurations
        pricing_configs = PricingConfig.objects.all()
        # Serialize and return the data
        serializer = PricingConfigSerializer(pricing_configs, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Deserialize the incoming data
        serializer = PricingConfigForm(data=request.data)
        
        if serializer.is_valid():
            # Save the new pricing configuration
            new_config = serializer.save()
            
            # Log the configuration change
            logger.info(f"Pricing configuration created: {new_config}")
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        # Retrieve existing pricing configuration
        pricing_config = get_object_or_404(PricingConfig, pk=pk)

        # Deserialize the incoming data with the instance
        serializer = PricingConfigForm(data=request.data, instance=pricing_config)
        
        if serializer.is_valid():
            # Save the modified pricing configuration
            updated_config = serializer.save()

            # Log the configuration change
            logger.info(f"Pricing configuration updated by {request.user}: {updated_config}")

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Retrieve existing pricing configuration
        pricing_config = get_object_or_404(PricingConfig, pk=pk)

        # Log the configuration removal
        logger.info(f"Pricing configuration deleted by {request.user}: {pricing_config}")

        # Delete the pricing configuration
        pricing_config.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class CalculatePricingAPIView(APIView):
    def post(self, request):
        # Extract necessary parameters from request data
        distance = Decimal(request.data.get('distance', 0))
        time = Decimal(request.data.get('time', 0))
        waiting_duration = Decimal(request.data.get('waiting_duration', 0))
        day_of_week = request.data.get('day_of_week', '')

        # Find the active pricing configuration for the given day
        pricing_config = get_object_or_404(PricingConfig, day_of_week=day_of_week, active=True)

        # Perform the pricing calculation
        price = (pricing_config.distance_base_price + (distance * pricing_config.distance_additional_price)) + (
                time * pricing_config.time_multiplier_factor) + (waiting_duration * pricing_config.waiting_charges)

        # Return the calculated price in the response
        return Response({'price': float(price)}, status=status.HTTP_200_OK)