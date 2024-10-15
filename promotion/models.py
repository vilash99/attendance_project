from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    ads_url = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.title
