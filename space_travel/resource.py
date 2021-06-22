from django.db import models


class Resource(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    weight = models.IntegerField(blank=False, default=0)