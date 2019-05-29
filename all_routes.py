import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import json
from graph import graph
plotly.tools.set_credentials_file(username='Ayoob', api_key='LyRWxrQ7Dhr6m2YZwOnf')


def plot_all(list2):

    for i in range(len(list2)):
        if len(list2[i]) < 6:
            list2[i].append(None)
            list2[i][len(list2[i])-1], list2[i][len(list2[i]) - 2] = list2[i][len(list2[i]) - 2], list2[i][len(list2[i])-1]
            list2[i][len(list2[i])-3], list2[i][len(list2[i]) - 2] = list2[i][len(list2[i]) - 2], list2[i][len(list2[i])-3]

    with open('cities_with_id.json', 'r') as f:
        cities = json.load(f)
    cities = cities['data']['cities']

    lats = []
    long = []
    l_lats = []
    l_long = []
    texts=['Malaysia', 'Singapore', 'Shanghai', 'Tokyo', 'Munich', 'London', 'Ontario', 'Virginia', 'Cairo', 'Dubai']

    for i in range(1,11):
        lats.append(cities[i]['lat'])
        long.append(cities[i]['long'])
        
        
    airports = [go.Scattergeo(
        lon = long,
        lat = lats,
        hoverinfo = 'text',
        text = texts,
        mode = 'markers',
        marker = go.scattergeo.Marker(
            size = 2,
            color = 'rgb(255, 0, 0)',
            line = go.scattergeo.marker.Line(
                width = 3,
                color = 'rgba(68, 68, 68, 0)'
            )
        ))]

    flight_paths = []
    for i in range(len(list2)):
        lats=[]
        long=[]
        
        for j in range(0, len(list2[i])-1):
            if list2[i][j] != None:
                lats.append(cities[list2[i][j]]['lat'])
                long.append(cities[list2[i][j]]['long'])
        
        l_lats.append(lats)
        l_long.append(long)
        

    for i in range(len(list2)):
        flight_paths.append(
            go.Scattergeo(
                lon = l_long[i],
                lat = l_lats[i],
                mode = 'lines',
                line = go.scattergeo.Line(
                    width = 1,
                    color = 'red',
                )
            )
        )
        
    layout = go.Layout(
        title = go.layout.Title(
            text = 'All Possible Flight Routes'
        ),
        showlegend = False,
        geo = go.layout.Geo(
            showland = True,
            landcolor = 'rgb(243, 243, 243)',
            countrycolor = 'rgb(204, 204, 204)',
        ),
    )

    fig = go.Figure(data = flight_paths + airports, layout = layout)
    py.plot(fig, filename = 'd3-flight-paths')