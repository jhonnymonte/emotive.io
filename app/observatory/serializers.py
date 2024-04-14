from rest_framework import serializers
from .models import Weather, SkyObject

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['city', 'temperature', 'feels_like', 'description', 'wind_speed', 'humidity', 'visibility', 'rain_volume']

class SkyObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkyObject
        fields = ['date', 'object_name', 'object_type', 'altitude', 'azimuth', 'constellation']

