from django.urls import path
from .views import WeatherDataAPIView, WeatherAndSkyObjectsAPIView, SavedSearchesAPIView

urlpatterns = [
    path('weather-data/', WeatherDataAPIView.as_view(), name='weather_data'),
    path('get-sky-objects/', WeatherAndSkyObjectsAPIView.as_view(), name='sky_and_objects'),
    path('saved-searches/', SavedSearchesAPIView.as_view(), name='saved_searches'),

    
]
