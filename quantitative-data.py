#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib


# In[2]:


file = 'exams.csv'


# In[3]:


df = pd.read_csv(file)
print(df.head())


# In[4]:


print(list(df))
print(len(df))


# In[13]:



col = 'reading score' #<-edit this value! column name as it appears in dataframe

col_name = 'reading score' #<-edit this value! descriptive name for column
freq = df[col].value_counts().rename_axis(col_name).reset_index(name='freq')
freq = freq.sort_values(by = col_name)
print(freq)


# In[8]:





# In[7]:


#create frequency chart
ax = freq.plot.barh(x=col_name, y='freq', rot=0)


# In[27]:


quant_col = 'reading score'
mean = df[quant_col].mean()
print(mean)

median = df[quant_col].median()
print(median)

standard_deviation = df[quant_col].std()
print(standard_deviation)


# In[ ]:





# In[ ]:




