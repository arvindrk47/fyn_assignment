def evaluate_price(config, distance, time):
    """
    Calculates the final invoice amount based on the time and distance traveled.

    Args:
        config (PricingConfig): The pricing config to use for the calculation.
        distance (float): The distance traveled in kilometers.
        time (float): The time taken in minutes.

    Returns:
        float: The final invoice amount.
    """
    tier = config.pricingtier_set.filter(distance_upto__gte=distance).first()
    if not tier:
        tier = config.pricingtier_set.first()

    base_price = tier.distance_upto * tier.distance_base_price
    additional_price = (distance - tier.distance_upto) * tier.distance_additional_price if tier.distance_additional_price else 0
    time_price = time * tier.time_multiplier_factor * tier.time_base_price
    waiting_price = (time - tier.waiting_time) * tier.waiting_charges if tier.waiting_charges else 0

    return base_price + additional_price + time_price + waiting_price