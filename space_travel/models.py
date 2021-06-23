from django.utils import timezone
from django.db import models


def certification_validate(numbers):
    certification = [int(char) for char in numbers if char.isdigit()]
    if len(certification) != 7:
        return False
    if certification == certification[::-1]:
        return False
    for i in range(6, 7):
        value = sum((certification[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != certification[i]:
            return False
    return True


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def field(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).field(**defaults)


class Pilot(models.Model):
    pilot_certification = models.BigIntegerField(blank=False, validators=[certification_validate])
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


class Ship(models.Model):
    fuel_capacity = models.IntegerField(blank=False)
    fuel_level = models.IntegerField(blank=False)
    weight_capacity = models.IntegerField(blank=False)
    created_at = models.DateTimeField(blank=False, default=timezone.now)
    disabled_at = models.DateTimeField(blank=False, default=None)
