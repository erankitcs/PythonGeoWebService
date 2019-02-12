from geopy.geocoders import Nominatim

def getgeocode(address):
    geolocator=Nominatim()
    location=geolocator.geocode(address,timeout=10)
    return location

##      print(getgeocode("735 Dolores St San Francisco CA 94119 USA"))
