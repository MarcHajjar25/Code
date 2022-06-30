#!/usr/bin/env python
# coding: utf-8

# In[16]:


#import necessary libaries
import pandas as pd
import matplotlib


# In[22]:


#name file path (you will have download your own dataset and populate the path and choose the appropriate cell to execute)
file = 'asecpub21csv/ffpub21.csv' # <-- edit this value! 


# In[23]:


#read data from CSV (.csv) & print head
df = pd.read_csv(file)
print(df.head())


# In[20]:


df = pd.read_csv('asecpub21csv/FRB_CP (1).csv')
print(df)


# In[24]:


print(list(df))
print(len(df))


# In[25]:


#output frequency table of chosen column in dataset
col = 'FKIND' #<-edit this value! column name as it appears in dataframe
col_name = 'Type of Family' #<-edit this value! descriptive name for column
freq = df[col].value_counts().rename_axis(col_name).reset_index(name='freq')
freq = freq.sort_values(by = col_name)
print(freq)


# In[26]:


#replace codes with descriptive labels
#if your dataframe already has descriptive labels, you don't need to run this cell
codebook = [['1', 'Married couple family'], #<- if appropriate, replace these values based on codebook or data dictionary for your dataset
            ['2', 'Male reference person'], 
            ['3', 'Female reference person']] 
#loops through label codes and replaces them in frequency table
for lbl in codebook:
    #use line below if codes are stored as integers
    freq[col_name] = freq[col_name].replace(int(lbl[0]), lbl[1])
    #use line below if codes are stored as strings
    #freq[col_name] = freq[col_name].replace(lbl[0], lbl[1])
#prints updated frequency table
print(freq)


# In[27]:


ax = freq.plot.barh(x=col_name, y='freq', rot=0)


# In[ ]:


col = 

