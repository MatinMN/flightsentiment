import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import json
from graph import graph

plotly.tools.set_credentials_file(username='Ayoob', api_key='LyRWxrQ7Dhr6m2YZwOnf')


def plot_shortest_path(path):

    with open('cities_with_id.json', 'r') as f:
        cities = json.load(f)

    cities = cities['data']['cities']

    lists = path
    lats = []
    long = []

    city = ''
    texts = []
    print(path)

    for i in range(len(lists)-1):
        lats.append(cities[lists[i]]['lat'])
        long.append(cities[lists[i]]['long'])
        city = cities[lists[i]]['name']
        texts.append(city)


    route = [go.Scattergeo(
        lat = lats,
        lon = long,
        mode = 'lines',
        text = texts,
        hoverinfo = 'text',
        line = go.scattergeo.Line(
            width = 2,
            color = 'blue',
        ),
    )]

    layout = go.Layout(
        title = go.layout.Title(
            text = 'Kuala Lumpur to ' + city
        ),
        showlegend = False,
        geo = go.layout.Geo(
            resolution = 50,
            showland = True,
            showlakes = True,
            landcolor = 'rgb(204, 204, 204)',
            countrycolor = 'rgb(204, 204, 204)',
            lakecolor = 'rgb(255, 255, 255)',
            projection = go.layout.geo.Projection(
                type = "equirectangular"
            ),
            coastlinewidth = 2,
            lataxis = go.layout.geo.Lataxis(
                range = [0, 70],
                showgrid = True,
                dtick = 10
            ),
            lonaxis = go.layout.geo.Lonaxis(
                range = [60, 190],
                showgrid = True,
                dtick = 20
            ),
        )
    )

    fig = go.Figure(data = route, layout = layout)
    py.plot(fig, filename = '+- bestpath')