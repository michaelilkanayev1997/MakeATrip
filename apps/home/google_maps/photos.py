# isntall the library
# pip install googlemaps
# pip install Pillow

# import the libraries
import googlemaps
# from PIL import Image

# Define the API Key.
API_KEY = 'AIzaSyBh0k7wq-khn5zdQsCD0q12iMKt6xVJl_M'
# AIzaSyBl-LW1ZgRQfQEicCI9Z_Di9755P4gc6ho
# API_KEY = 'AIzaSyAer4VW66byYQj08TzM2LYzWcRy2xcy_B8'

# Define the Client
gmaps = googlemaps.Client(key=API_KEY)


def place_search():
    places_result = gmaps.places_nearby(location='31.2381647,34.7931273', radius=10000)

    for place in places_result['results']:

        my_place_id = place['place_id']

        my_fields = ['name', 'formatted_phone_number', 'photo']

        places_details = gmaps.place(place_id=my_place_id, fields=my_fields)

        for photo in places_details['result']['photos']:
            photo_id = photo['photo_reference']
            photo_width = 1200
            photo_height = 1200

            url = "https://maps.googleapis.com/maps/api/place/photo?photoreference={0}&sensor=false&maxheight={1}" \
                  "&maxwidth={2}&key={3}".format(photo_id, photo_width, photo_height, API_KEY)

            print(url)


place_search()

# {'lat': 31.2445217197085, 'lng': 34.7949667697085}}}