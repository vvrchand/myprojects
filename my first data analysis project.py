#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv(r"C:\Users\vvrch\OneDrive\Desktop\CLEAN_FIFA23_official_data.csv")


# In[2]:


data


# In[3]:


head()


# In[4]:


data.head()


# In[5]:


data.tail()


# In[6]:


data.shape()


# In[7]:


data.shape


# In[8]:


data.size


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[11]:


data.info()


# In[12]:


data.shape


# In[13]:


data[data.duplicated()]


# In[15]:


data.drop_duplicates(implace = True)


# In[17]:


data.drop_duplicates(implace = True)


# In[ ]:




