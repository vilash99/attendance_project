from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'ads_url', 'image_url')


admin.site.register(Advertisement, AdvertisementAdmin)
