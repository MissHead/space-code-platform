from django.utils import timezone
from django.db import models
from space_travel.helpers import certification_validate

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def field(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).field(**defaults)


class Pilot(models.Model):
    pilot_certification = models.CharField(max_length=7, blank=False, validators=[certification_validate])
    name = models.CharField(max_length=70, blank=False)
    age = IntegerRangeField(min_value=1, max_value=100)
    credits = models.IntegerField(blank=False, default=0)
    location_planet = models.CharField(max_length=70, blank=False)
    created_at = models.DateTimeField(blank=False, default=timezone.now)
    disabled_at = models.DateTimeField(blank=False, default=None)


class Resource(models.Model):
    name = models.CharField(max_length=70, blank=False)
    weight = models.IntegerField(blank=False)
    created_at = models.DateTimeField(blank=False, default=timezone.now)
    disabled_at = models.DateTimeField(blank=False, default=None)


class Contract(models.Model):
    description = models.CharField(max_length=200,blank=False)
    payload = models.JSONField(blank=False, default=dict)
    origin_planet = models.CharField(max_length=70, blank=False)
    destination_planet = models.CharField(max_length=70, blank=False)
    value = models.IntegerField(blank=False)
    created_at = models.DateTimeField(blank=False, default=timezone.now)
    disabled_at = models.DateTimeField(blank=False, default=None)


class Ship(Pilot):
    fuel_capacity = models.IntegerField(blank=False)
    fuel_level = models.IntegerField(blank=False)
    weight_capacity = models.IntegerField(blank=False)
