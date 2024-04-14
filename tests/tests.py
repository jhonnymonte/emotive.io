from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class WeatherDataAPITestCase(APITestCase):
    def test_weather_data_view(self):
        url = reverse('weather-data')
        response = self.client.get(url, {'latitude': 40.7128, 'longitude': -74.0060})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class WeatherAndSkyObjectsAPITestCase(APITestCase):
    def test_weather_and_sky_objects_view(self):
        url = reverse('weather-sky-objects')
        response = self.client.get(url, {'latitude': 40.7128, 'longitude': -74.0060})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class SavedSearchesAPITestCase(APITestCase):
    def test_saved_searches_view(self):
        url = reverse('saved-searches')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_saved_searches_view_with_date(self):
        url = reverse('saved-searches')
        response = self.client.get(url, {'date': '2024-04-14'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
