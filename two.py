#!/usr/bin/env python
# coding: utf-8

# In[12]:


import astropy
import pandas as pd


# In[13]:

def plot():

    df = pd.read_csv("data.csv")


    # In[18]:


    rs= []
    for i in range(274):
        rs.append(df.loc[:, "Column 7"][i])

    ebv= []
    for i in range(274):
        ebv.append(df.loc[:, "Column 10"][i])

    idi= []
    for i in range(274):
        idi.append(df.loc[:, "Column 1"][i])

    distmod= []
    for i in range(274):
        distmod.append(df.loc[:, "Column 9"][i])


    # In[19]:


    ratio = []
    for i in range(274):
        ratio.append(rs[i] + 1)


    # In[20]:


    distance = []
    for i in range(274):
        x = (distmod[i] + 5)/5
        distance.append(10**x)


    # In[23]:


    from plotly.offline import iplot


    # In[24]:



    import plotly.plotly as py
    import plotly.graph_objs as go


    # In[25]:


    trace = go.Scatter(
        x = ratio,
        y = distmod,
        mode = "markers"
    )


    # In[26]:


    data = [trace,]

    a = []
    for i in range(274):
        if (rs[i] < 0.000847):
            a.append(idi[i]+1)
    
    a = "The sources which lie inside Milky way are: " + ", ".join(map(str, a))

    return data, a
