import requests
import json
import urllib.parse
from utils import *


def addressLookup(address):
    keyData = open_file('mapsDataKeys.txt')
    main_api = keyData[0].replace('\n', '')
    key = keyData[1]

    url = main_api + urllib.parse.urlencode({'address': address}) + key
    
    data = requests.get(url).json()
    
    try:
        formatted_address = data['results'][0]['formatted_address']
        latitude = data['results'][0]['geometry']['location']['lat']
        longitude = data['results'][0]['geometry']['location']['lng']
        map_location = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + "," + str(longitude)
    
    except:
        return None, None
    
    return formatted_address, map_location

#addressLookup('edmonton')



