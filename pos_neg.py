#!/usr/bin/env python
# coding: utf-8

# In[26]:


import plotly.plotly as py
import plotly.graph_objs as go
import plotly

plotly.tools.set_credentials_file(username='abdrsh', api_key='soOFfebkRlafYkLGAijA')


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


# In[ ]:




