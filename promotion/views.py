import random
from .models import Advertisement


def get_random_ads():
    """
    Get random advertisement from list
    """
    ads_list = Advertisement.objects.all()
    if ads_list:
        return random.choice(ads_list)
    return None
