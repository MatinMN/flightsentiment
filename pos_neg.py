#!/usr/bin/env python
# coding: utf-8

# In[26]:


import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from helper import *
plotly.tools.set_credentials_file(username='Ayoob', api_key='LyRWxrQ7Dhr6m2YZwOnf')


def pos_neg(countries): 
    
    pos=[]
    neg = []
    lc = []
    for country in countries:
        pos.append(countries[country]['positive'])
        neg.append(countries[country]['negative'])
        lc.append(country)

    data = [
      go.Bar(
        y = pos,
        x = lc,
        name = "positive"
      ),
      go.Bar(
        y = neg,
        x = lc,
        name = "negative"
      )
    ]

    layout = go.Layout(
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='+- function')



def stop_words(freq_arr,name): 
    
    stops = STOPLIST
    freq = []
    for word in STOPLIST:
       if word in freq_arr:
          freq.append(freq_arr[str(word)])
       else:
          freq.append(0)

    data = [
      go.Bar(
        y = freq,
        x = stops,
        name = "frequency"
      )
    ]

    layout = go.Layout(
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='+- '+name)


# In[ ]:




