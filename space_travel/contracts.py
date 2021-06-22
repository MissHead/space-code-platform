from django.db import models


class Contracts(models.Model):
    description = models.CharField(max_length=200,blank=False, default='')
    payload = models.JSONField(blank=False, default={})
    origin_planet = models.CharField(max_length=70, blank=False, default='')
    destination_planet = models.CharField(max_length=70, blank=False, default='')
    value = models.IntegerField(blank=False, default=0)