#!/usr/bin/env python
# coding: utf-8

# In[17]:


import plotly.plotly as py
import plotly.graph_objs as go
import plotly

plotly.tools.set_credentials_file(username='abdrsh', api_key='soOFfebkRlafYkLGAijA')

lines = [line.rstrip('\n') for line in open('stop words.txt')]


def stop_words(countries):
    
    #store the list of countries
    lc = [*countries]

    #different markers for different cities
    colors = ['rgb(0,0,0)', 'rgb(255, 0, 0)', 'rgb(0,255,0)', 'rgb(0, 0, 255)', 'rgb(255, 255, 0)', 'rgb(128, 0, 128)', 'rgb(255, 0, 255)', 'rgb(0, 255, 255)', 'rgb(128, 128, 128)']
    count=0

    #plotly traces
    data = []
    
    for xs in lc:
        
        #store the frequency of stop words of each city into a dictionary
        values=[]
        for i in lines:
            if countries.get(xs).get(i) != None:
                values.append(countries.get(xs).get(i))
            else:
                values.append(0)
            

        #plotly traces
        trace = go.Scatter(
            x = lines,
            y = values,
            name = xs,
            line = dict(
                color = (colors[count]),
                width = 4)
            )
    
        count+=1
        data.append(trace)

    # Edit the layout
    layout = dict(title = 'Frequency of Stop Words',
                  xaxis = dict(title = 'Stop Words'),
                  yaxis = dict(title = 'Count'),
                  )

    fig = dict(data=data, layout=layout)
    py.plot(fig, filename='styled-line')

