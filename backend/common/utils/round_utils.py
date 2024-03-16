# Needed to round prices in rial or Toman


def round_to_nearest_thousand(value):
    # round 000  ex)   35378 -> 35000
    return round(value / 1000) * 1000


def round_to_nearest_hundred(value):
    # round 000  ex)   35378 -> 35300
    return round(value / 100) * 100
