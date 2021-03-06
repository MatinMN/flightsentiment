from __future__ import division
from sentiment import *
from graph import graph
from pos_neg import *
from maper import *
from all_routes import *

print("Welcome to the flightsentiment app")
print("Enter Name of the city you like to travel to :")
print("singapore, tokyo, shanghai, munich, virginia, ontario, london, cairo, dubai")
print("Choose one destination please")

print('----------------------------------------------------------------------------')
dictionary = get_cities()
city_code = raw_input()


city_code = dictionary[str(city_code)]['id']

sentiment_results = get_sentiment()
paths = graph.getShortestPaths(1,city_code)

city_names = get_countries()

sentiment_value = []
path_scores = []

min_score = 99999
best_path = []
for path in paths:
    print(path)
    sentiment_score = 0
    path_score = 0
    for i in range(1,len(path)-2):
        node_id = path[i]
        node_name = city_names[node_id]["name"]
        pos = sentiment_results[node_name]['positive']
        neg = sentiment_results[node_name]['negative']
        s = pos+neg
        if(s != 0):
            sentiment_score += int((pos / (pos + neg) )* 100)
    
    sentiment_score *= 1
    path_score += path[len(path)-1]
    path_score -= sentiment_score
    path_scores.append(path_score)
    if path_score < min_score:
        min_score = path_score
        best_path = path

    sentiment_value.append(sentiment_score)    

print(sentiment_value)
print(path_scores)
print("this is the best path")
print(best_path)

print("Ploting best path")
plot_shortest_path(best_path)

plot_all(graph.getAllPossiblePaths())


pos_neg(sentiment_results)
for i in range(1,len(city_names)):
    name = city_names[i]['name']
    stop_words(sentiment_results[name]['word_freq'],name)

