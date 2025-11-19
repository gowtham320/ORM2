from django.db import models
from django.contrib import admin
class car(models.Model):
    brand = models.CharField(max_length=10)
    car_name = models.CharField(max_length=10)
    enginenum = models.IntegerField()
    release = models.DateField()

class carAdmin(admin.ModelAdmin):
    list_display=('brand', 'car_name', 'enginenum', 'release')