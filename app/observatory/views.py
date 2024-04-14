
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Weather, SkyObject
from .serializers import WeatherSerializer, SkyObjectSerializer
from datetime import datetime

from .utils import get_weather_data, get_sky_objects


class WeatherDataAPIView(APIView):
    def get(self, request):
        
        latitude = request.query_params.get('latitude', None)
        longitude = request.query_params.get('longitude', None)

        # Validar que se proporcionen todos los parámetros necesarios
        if not all([latitude, longitude]):
            return Response({"error": "Missing query parameters"}, status=400)

        # Obtener datos del clima utilizando la función de utilidad
        weather_data = get_weather_data(latitude, longitude)

        return Response(weather_data)


class WeatherAndSkyObjectsAPIView(APIView):
    def get(self, request):
        latitude = request.query_params.get('latitude', None)
        longitude = request.query_params.get('longitude', None)

        weather_data = get_weather_data(latitude, longitude)

        sky_objects_data = get_sky_objects(latitude, longitude)

        weather = Weather.objects.create(
            city=weather_data['name'],
            temperature=weather_data['main']['temp'],
            feels_like=weather_data['main']['feels_like'],
            description=weather_data['weather'][0]['description'],
            wind_speed=weather_data['wind']['speed'],
            humidity=weather_data['main']['humidity'],
            visibility=weather_data['visibility'],
            rain_volume=weather_data['rain'].get('1h') if 'rain' in weather_data else None
        )

        for entry in sky_objects_data['data']['table']['rows']:
            for cell in entry['cells']:
                SkyObject.objects.create(
                    date=cell['date'],
                    object_name=cell['name'],
                    object_type=entry['entry']['id'],
                    altitude=float(cell['position']['horizontal']['altitude']['degrees']),
                    azimuth=float(cell['position']['horizontal']['azimuth']['degrees']),
                    constellation=cell['position']['constellation']['name']
                )

        weather_serializer = WeatherSerializer(weather)
        sky_objects_serializer = SkyObjectSerializer(SkyObject.objects.all(), many=True)
        return Response({
            "weather": weather_serializer.data,
            "sky_objects": sky_objects_serializer.data
        })


class SavedSearchesAPIView(APIView):
    def get(self, request):
        date_param = request.query_params.get('date', None)

        if date_param:
            try:
                date = datetime.strptime(date_param, '%Y-%m-%d').date()
            except ValueError:
                return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)
            
            sky_object_searches = SkyObject.objects.filter(date__date=date)


            weather_searches = Weather.objects.filter(timestamp__date=date)
        else:
            sky_object_searches = SkyObject.objects.all()

            weather_searches = Weather.objects.all()

        weather_serializer = WeatherSerializer(weather_searches, many=True)
        sky_object_serializer = SkyObjectSerializer(sky_object_searches, many=True)

        response_data = {
            "weather_searches": weather_serializer.data,
            "sky_object_searches": sky_object_serializer.data
        }

        return Response(response_data)



