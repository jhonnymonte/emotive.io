# Take Home - Django Skeleton

## Getting Started
Dependencies:
* Docker - See [Get Docker](https://docs.docker.com/get-docker/)
* Docker Compose - Installed with Docker Desktop, See [Install Docker Compose](https://docs.docker.com/compose/install/)

With the dependencies installed, running the project is as simple as running:
```bash
docker compose up
```

This will pull the required Docker images and spin up a container running your service on http://localhost:8000.

To end the service, press `Ctrl+C`

## Weather and Celestial Objects API Project

This project consists of an API developed with Django that provides weather data and information about celestial objects. The API allows querying for weather information at a specific location, as well as data about celestial objects visible in the sky at a given location and time.

## Key Features
* Weather Data Query: The API provides an endpoint /weather-data/ allowing retrieval of weather data for a specific location, specified by latitude and longitude.
* Celestial Objects Query: The API provides an endpoint /get-sky-objects/ allowing retrieval of information about celestial objects visible in the sky at a specific location, also specified by latitude and longitude.
* Saved Searches Query: The API provides an endpoint /saved-searches/ allowing retrieval of previous search data, either for weather data or celestial objects, optionally filtered by date.

## Using the API
Once the server is up and running, you can access the API endpoints using tools like curl, Postman, or simply by browsing in your web browser. Below are the available endpoints:

* Weather data query: http://localhost:8000/weather-data/?latitude={latitude}&longitude={longitude}
* Celestial objects query: http://localhost:8000/get-sky-objects/?latitude={latitude}&longitude={longitude}
* Saved searches query: http://localhost:8000/saved-searches/

# Replace {latitude} and {longitude} with the corresponding latitude and longitude values of the desired location.

## URL example

* California
http://localhost:8000/weather-data/?latitude=36.7783&longitude=-119.4179
http://localhost:8000/get-sky-objects/?latitude=36.7783&longitude=-119.4179

* Bahia Blanca
http://localhost:8000/weather-data/?latitude=-38.7196&longitude=-62.2724
http://localhost:8000/get-sky-objects/?latitude=-38.7196&longitude=-62.2724

* Saved Search filter by date
http://localhost:8000/observatory/saved-searches/?date=2024-04-13