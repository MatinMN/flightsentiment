import requests, json
from math import cos, asin, sqrt


PARAMS = {'distance' : 'goole'}
cities = open('cities.txt')
lng_lat = open('lat&lng.txt', 'a')
count = 0
city_in_number = 1
url = 'https://maps.googleapis.com/maps/api/geocode/json?address=international_airport+'
apiKey = '&key=AIzaSyDXx1fcx1Qr9gEaHiOjfp8isEVRqD5fiY0'


for city in cities:
    word = city.split(' ')
    # print (city)
    urlGet =  url + word[0] + apiKey
    googleResponse = requests.get(url = urlGet, params = PARAMS)
    data = googleResponse.json()
    data = data['results']
    # print (data)
    coordinates = str(city_in_number) + " " + str(data[0]['geometry']['location']['lat']) + " " + str(data[0]['geometry']['location']['lng']) + " s"
    print(coordinates)
    lng_lat.write(coordinates + "\n")
    urlGet = ''
    city_in_number = city_in_number+1
