from django.db import models
from django.forms import ModelForm

class Profiles(models.Model):
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    age = models.IntegerField(default='0')
    gender = models.IntegerField(default='0')
    ta_m = models.FloatField(default='0')
    va_m = models.FloatField(default='0')
    trav = models.FloatField(default='0')
    velav = models.FloatField(default='0')
    met = models.FloatField(default='0')
    clo = models.FloatField(default='0')
    da15_ta = models.FloatField(default='0')
    da6_ta = models.FloatField(default='0')
    daav_ta = models.FloatField(default='0')
    da15_rh = models.FloatField(default='0')
    da6_rh = models.FloatField(default='0')
    daav_rh = models.FloatField(default='0')





