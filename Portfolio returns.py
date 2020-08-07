#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[4]:


tickers = ['PG', 'MSFT', 'F', 'GE']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source = 'yahoo', start = '1995-1-1')['Adj Close']


# In[8]:


mydata.head()


# In[9]:


mydata.tail()


# In[12]:


mydata.iloc[0]


# In[15]:


(mydata/mydata.iloc[0]*100).plot(figsize = (15,6))
mydata


# In[17]:


mydata.loc['1995-01-03']


# In[19]:


mydata.iloc[0]


# In[20]:


returns = (mydata/mydata.shift(1)) - 1
returns.head()


# In[22]:


weights = np.array([0.25, 0.25, 0.25, 0.25])


# In[23]:


np.dot(returns , weights)


# In[24]:


annual_returns = returns.mean()* 250
annual_returns


# In[25]:


np.dot(annual_returns, weights)


# In[37]:


pfolio_1 = (str(round(np.dot(annual_returns, weights), 3)* 100) + '%')


# In[38]:


print(pfolio_1)


# In[39]:


weights_2 = np.array([0.4,0.4,0.15,0.05])


# In[40]:


pfolio_2 = (str(round(np.dot(annual_returns, weights_2), 3)* 100) + '%')


# In[41]:


print(pfolio_2)


# In[42]:


if pfolio_1>pfolio_2:
    print('First is better')
elif pfolio_1<pfolio_2:
        print('Second is better')
else:
    print('They are equally good')


# In[ ]:




