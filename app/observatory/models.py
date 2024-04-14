from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    feels_like = models.FloatField()
    description = models.CharField(max_length=100)
    wind_speed = models.FloatField()
    humidity = models.IntegerField()
    visibility = models.IntegerField()
    rain_volume = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Weather in {self.city} - {self.timestamp}"

class SkyObject(models.Model):
    date = models.DateTimeField()
    object_name = models.CharField(max_length=100)
    object_type = models.CharField(max_length=100)
    altitude = models.FloatField()
    azimuth = models.FloatField()
    constellation = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.object_name} - {self.date}"
