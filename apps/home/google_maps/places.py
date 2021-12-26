from django.utils.http import urlquote
from geopy.geocoders import Nominatim
import time
import csv
from googlemaps.places import places_nearby as g_places_nearby
from googlemaps.places import place as g_place
import googlemaps

"""

AIzaSyAKBPc2d9ZAGhe3vt8SgGmAgoZdOHXECW8





"""
# API_KEY = 'AIzaSyA3L3Q5rCMHsMgixN6s6x9Y7vaSOHLSoJ4'
API_KEY = 'AIzaSyBh0k7wq-khn5zdQsCD0q12iMKt6xVJl_M'
gmaps = googlemaps.Client(key=API_KEY)


class GooglePlaces(object):
    def __init__(self, destination, types):
        self.destination = destination
        self.types = types
        self.data = {
            "name": [],
            "address": [],
            "phone_number": [],
            "opening_hours": [],
            "rating": [],
            "location": [],
            "photo": [],
            "types": [],
        }
        self.places = []

    def get_name(self):
        return self.data['name']

    def get_address(self):
        return self.data['address']

    def get_phone_number(self):
        return self.data['phone_number']

    def get_opening_hours(self):
        return self.data['opening_hours']

    def get_rating(self):
        return self.data['rating']

    def get_location(self):
        return self.data['location']

    def get_photo(self):
        return self.data['photo']

    def get_type(self):
        return self.data['types']

    def get_places(self):
        return self.places

    def search_places_by_coordinate(self):
        # convert destination name to latitude and longitude
        geolocator = Nominatim(user_agent="Your_Name")
        location = geolocator.geocode(self.destination)
        lat_long = (location.latitude, location.longitude)

        places_result = g_places_nearby(client=gmaps, location=lat_long, radius=50000, type=self.types)
        # print(places_result)

        self.places.extend(places_result['results'])
        while "next_page_token" in places_result:
            time.sleep(2)
            places_result = g_places_nearby(client=gmaps, page_token=places_result['next_page_token'])
            self.places.extend(places_result['results'])

        return places_result

    def get_place_details(self, place_id, fields):

        details = g_place(client=gmaps, place_id=place_id, fields=fields)
        return details

    def get_data(self):
        fields = [
            'name',
            'formatted_address',
            'formatted_phone_number',
            'opening_hours',
            'type',
            'rating',
            'geometry',
            'photo',
        ]
        for place in self.places:
            details = self.get_place_details(place.get('place_id'), fields)
            try:
                name = details['result'].get('name')
                self.data['name'].append(name)
            except KeyError:
                name = "None"
                self.data['name'].append(name)

            try:
                address = details['result'].get('formatted_address')
                self.data['address'].append(address)
            except KeyError:
                address = "None"
                self.data['address'].append(address)

            try:
                opening_hours = details['result'].get('opening_hours', {}).get('weekday_text')
                self.data['opening_hours'].append(opening_hours)
            except KeyError:
                opening_hours = "None"
                self.data['opening_hours'].append(opening_hours)

            try:
                phone_number = details['result'].get('formatted_phone_number')
                self.data['phone_number'].append(phone_number)
            except KeyError:
                phone_number = "None"
                self.data['phone_number'].append(phone_number)

            try:
                rating = details['result'].get('rating')
                self.data['rating'].append(rating)
            except KeyError:
                rating = "None"
                self.data['rating'].append(rating)

            try:
                types = details['result'].get('types')
                self.data['types'].append(types)
            except KeyError:
                types = "None"
                self.data['types'].append(types)

            try:
                lat = details['result']['geometry']['location']['lat']
                lng = details['result']['geometry']['location']['lng']
                location = '{0},{1}'.format(lat, lng)
                self.data['location'].append(location)
            except KeyError:
                lat = "None"
                lng = "None"
                location = '{0},{1}'.format(lat, lng)
                self.data['location'].append(location)

            try:
                for photo in details['result']['photos']:
                    photo_id = photo['photo_reference']
                    photo_width = 1200
                    photo_height = 1200

                    url = "https://maps.googleapis.com/maps/api/place/photo?photoreference={0}&sensor=false&maxheight={1}" \
                          "&maxwidth={2}&key={3}".format(photo_id, photo_width, photo_height, API_KEY)

                    # print(url)
                    break
            except KeyError:
                lat = "None"
                lng = "None"
                location = '{0},{1}'.format(lat, lng)
                self.data['location'].append(location)

        return self.data

    def get_google_image_search_url(self, place):
        pass


# google_places = GooglePlaces('Eilat', 'campground')
# google_places.search_places_by_coordinate()
# google_places.get_data()
# print((google_places.get_name()))
# print((google_places.get_name()))
# print((google_places.get_address()))
# print((google_places.get_opening_hours()))
# print((google_places.get_rating()))
# print((google_places.get_phone_number()))
# print((google_places.get_location()))
# print((google_places.get_google_image_search_url('BarBaSaba Beer Garden')))
