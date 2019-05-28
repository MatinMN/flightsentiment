import requests, json
from math import cos, asin, sqrt


PARAMS = {'distance' : 'google'}
cities = open('cities.txt')
lat_long = open('lat_long.txt', 'a')
count = 0
city_in_number = 1
url = 'https://maps.googleapis.com/maps/api/geocode/json?address=Airport+'
apiKey = '&key=AIzaSyDXx1fcx1Qr9gEaHiOjfp8isEVRqD5fiY0'


for city in cities:
    word = city.split(' ')
    # print (word[1])
    urlGet =  url + word[1] + apiKey
    googleResponse = requests.get(url = urlGet, params = PARAMS)
    data = googleResponse.json()
    data = data['results']
    # print (data)
    coordinates = str(city_in_number) + " " + str(data[0]['geometry']['location']['lat']) + " " + str(data[0]['geometry']['location']['lng']) + " s"
    print(coordinates)
    lat_long.write(coordinates + "\n")
    urlGet = ''
    city_in_number = city_in_number+1
