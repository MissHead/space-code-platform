from django.db import models


class Pilot(models.Model):
    fuel_capacity = models.IntegerField(blank=False, default=0)
    fuel_level = models.IntegerField(blank=False, default=0)
    weight_capacity = models.IntegerField(blank=False, default=0)