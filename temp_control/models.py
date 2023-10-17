from django.db import models


class Room(models.Model):
    cooler_status = models.BooleanField(default=False)
    heater_status = models.BooleanField(default=False)
    is_automatic = models.BooleanField(default=False)


class Weather(models.Model):
    city_temperature = models.IntegerField()
    city_weather_condition = models.CharField(max_length=200)
