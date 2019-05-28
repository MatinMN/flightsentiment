#!/usr/bin/env python
# coding: utf-8

# In[26]:


import plotly.plotly as py
import plotly.graph_objs as go
import plotly

plotly.tools.set_credentials_file(username='abdrsh', api_key='soOFfebkRlafYkLGAijA')

result = {"positive": 0, "negative": 10}
countries = {"Kuala Lumpur": result}

result = {"positive": 16.5, "negative": 5}
countries['Singapore'] = result
def pos_neg(countries): 
    lc = [*countries]
    pos=[]
    neg = []

    for i in range(len(lc)):
        pos.append(countries.get(lc[i]).get('positive'))
        neg.append(countries.get(lc[i]).get('negative'))

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
    py.iplot(fig, filename='+- function')


# In[ ]:




