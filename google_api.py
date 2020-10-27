import googlemaps
from datetime import datetime
import requests
import numpy as np
import json
from googlegeocoder import GoogleGeocoder

import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

"""
    In order to access the api key:
    
    Create a .env file (touch .env) and add the api key. The api key can be found
    in google cloud console.
"""
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
geocoder = GoogleGeocoder(GOOGLE_MAPS_API_KEY)

"""
    Try this commented block to get a feel of how the maps api handles geocoding.
    There are several ways of accessing a specific coordinate.

geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print(geocode_result, "\n")
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
print(reverse_geocode_result)
"""

"""
    Code below:
    Reverse geocoding on a peninsula in Azerbaijan: ref coordinates.
    Done the same for (lat, lng) = (0, 0) in the Atlantic ocean (rougly bay of guinea).

    Reverse geocoding seems to only return valuable into for a specific coordinate on land.
    This can be used as a safety net to govern ground truth for water/land.
    Detecting color of pixel in road map should be the first check though.
"""
peninsula_azerbaijan = gmaps.reverse_geocode((40.247393, 50.364690))
print(peninsula_azerbaijan)

atlantic_ocean = gmaps.reverse_geocode((0, 0))
print(atlantic_ocean)




"""
    Code that generates images from google. Both roadmaps and satllite images.
    The thought here is that the satelite images are used for training and roadmap images
    are used as ground truth.
"""
def create_images(lat, lng, zoom):
    
    maptype = ['satellite', 'roadmap']
    size = '300x300'
    for i in range(len(zoom)):
        center = str(lat[i]) + ',' + str(lng[i])
        for j in range(len(maptype)):
            URL = 'https://maps.googleapis.com/maps/api/staticmap?center='+center+'&zoom='+str(zoom[i])+'&size='+size+'&maptype='+maptype[j]+'&key='+GOOGLE_MAPS_API_KEY
            respone = requests.get(URL)
            with open('./images/'+center+','+maptype[j]+'.png', 'wb') as file:
                file.write(respone.content)

lat = [64.43, 59.85]
lng = [10.39, 10.65]
zoom = [14, 12]

create_images(lat, lng, zoom)
