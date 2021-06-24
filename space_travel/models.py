import datetime
from django.utils import timezone
from django.db import models


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def field(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).field(**defaults)


class Planet(models.Model):
    name = models.CharField(max_length=70, blank=False)
    created_at = models.DateTimeField(blank=False, default=timezone.now)
    disabled_at = models.DateTimeField(blank=False, default=None)

    def delete(self):
        self.disabled_at = datetime.datetime.now()
        self.save()


class Pilot(models.Model):
    pilot_certification = models.CharField(max_length=7, blank=False)
    name = models.CharField(max_length=70, blank=False)
    age = IntegerRangeField(min_value=1, max_value=100)
    credits = models.IntegerField(blank=False, default=0)
    location_planet = models.ForeignKey('Planet', related_name='%(class)s_location', on_delete=models.CASCADE, blank=False)
    created_at = models.DateTimeField(blank=False, default=timezone.now)
    disabled_at = models.DateTimeField(blank=False, default=None)

    def delete(self):
        self.disabled_at = datetime.datetime.now()
        self.save()


class Resource(models.Model):
    name = models.CharField(max_length=70, blank=False)
    weight = models.IntegerField(blank=False)
    created_at = models.DateTimeField(blank=False, default=timezone.now)
    disabled_at = models.DateTimeField(blank=False, default=None)

    def delete(self):
        self.disabled_at = datetime.datetime.now()
        self.save()


class Travel(models.Model):
    origin_planet = models.ForeignKey('Planet', related_name='%(class)s_origin', on_delete=models.CASCADE, blank=False)
    destination_planet = models.ForeignKey('Planet', related_name='%(class)s_destination', on_delete=models.CASCADE, blank=False)
    route = models.JSONField(blank=False, default=dict)
    fuel_costs = models.IntegerField(blank=False)
    created_at = models.DateTimeField(blank=False, default=timezone.now)
    disabled_at = models.DateTimeField(blank=False, default=None)

    def delete(self):
        self.disabled_at = datetime.datetime.now()
        self.save()


class Contract(models.Model):
    description = models.CharField(max_length=200,blank=False)
    payload = models.JSONField(blank=False, default=dict)
    origin_planet = models.ForeignKey('Planet', related_name='%(class)s_origin', on_delete=models.CASCADE, blank=False)
    destination_planet = models.ForeignKey('Planet', related_name='%(class)s_destination', on_delete=models.CASCADE, blank=False)
    value = models.IntegerField(blank=False)
    pilot = models.ForeignKey('Pilot', on_delete=models.CASCADE, blank=False)
    travel = models.ForeignKey('Travel', on_delete=models.CASCADE, blank=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=False, default=timezone.now)
    disabled_at = models.DateTimeField(blank=False, default=None)

    def delete(self):
        self.disabled_at = datetime.datetime.now()
        self.save()


class Ship(models.Model):
    fuel_capacity = models.IntegerField(blank=False)
    fuel_level = models.IntegerField(blank=False)
    weight_capacity = models.IntegerField(blank=False)
    pilot = models.ForeignKey('Pilot', on_delete=models.CASCADE, blank=False)
    created_at = models.DateTimeField(blank=False, default=timezone.now)
    disabled_at = models.DateTimeField(blank=False, default=None)

    def delete(self):
        self.disabled_at = datetime.datetime.now()
        self.save()
