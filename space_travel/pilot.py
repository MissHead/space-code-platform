from django.db import models
from helpers import certification_validate

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
    name = models.CharField(max_length=70, blank=False, default='')
    age = IntegerRangeField(min_value=1, max_value=100)
    credits = models.IntegerField(blank=False, default=0)
    location_planet = models.CharField(max_length=70, blank=False, default='')