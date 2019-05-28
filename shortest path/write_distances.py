from math import cos, asin, sqrt

# Open files..
lng_lat = open('lat&lng.txt')
graph = open('graph.txt')
weighted_graph = open('weighted_graph.txt', 'a')

# A function to calculate the straight line between two points..
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin...

count = 1
city_in_number = 1

edge_lng_lat = {}
distances = {}

for city in lng_lat:
    city = city.split(' ')
    edge_lng_lat[count] = city
    print(city)
    count = count + 1
print (edge_lng_lat)

for edge in graph:
    edge = edge.split(' ')
    print (edge)
    vertex1 = edge_lng_lat[int(edge[0])]
    vertex2 = edge_lng_lat[int(edge[1])]
    distance_value = distance(float(vertex1[1]), float(vertex1[2]), float(vertex2[1]), float(vertex2[2]))
    print(distance_value)
    weighted_graph.write(str(edge[0]) + " " + str(edge[1]) + " " + str(int(distance_value)) + " s" +"\n")
