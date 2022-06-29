#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


#import numpy
import numpy as np 


# In[20]:


df = pd.read_csv('asecpub21csv/FRB_CP (1).csv')
print(df)


# In[21]:


df = pd.DataFrame(np.random.randint(0,100, size = (1000,12)), columns = list('ABCDEFGHIJKL'))
print(df)


# In[13]:


#print first five rows of dataset
print(df.head())


# In[8]:


list (df)


# In[ ]:




