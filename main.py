from sentiment import *
from graph import graph
from pos_neg import *

print("Welcome to the flightsentiment app")
print("Enter which cities you would like to travel to :")
city_code = input()

sentiment_results = get_sentiment()
print(graph.getPaths(1,city_code))


pos_neg(sentiment_results)
