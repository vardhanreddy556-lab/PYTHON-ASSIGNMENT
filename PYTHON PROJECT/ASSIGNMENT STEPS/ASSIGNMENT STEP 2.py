#!/usr/bin/env python
# coding: utf-8

# In[1]:


#IMPORT PANDAS


# In[48]:


import pandas as pd


# In[3]:


#READ THE CSV FILE


# In[49]:


df = pd.read_csv("raw_products.csv")


# In[5]:


#DISPLAY THE FIRST 5 ROWS


# In[50]:


df.head()


# In[5]:


#CHECK THE SHAPE OF THE DATA


# In[51]:


print(df.shape)


# In[9]:


#CHECK THE COLUMN NAMES


# In[52]:


print(df.columns)


# In[11]:


#CHECK THE DATA TYPES


# In[53]:


print(df.dtypes)


# In[13]:


#CHECK FOR MISSING VALUES


# In[54]:


print(df.isnull().sum())


# In[15]:


#REMOVE DUPLICATE ROWS


# In[55]:


df = df.drop_duplicates()


# In[56]:


print(df.shape)


# In[9]:


#CLEAN THE PRICE COLUMN


# In[57]:


df["Price"] = df["Price"].astype(str)
df["Price"] = df["Price"].str.replace("Â£", "", regex=False)
df["Price"] = df["Price"].str.replace("£", "", regex=False)
df["Price"] = df["Price"].astype(float)


# In[58]:


print(df["Price"].head())


# In[59]:


df.dtypes


# In[24]:


#DISPLAY THE CLEANED DATA


# In[60]:


print(df.head())


# In[30]:


#SAVE THE CLEANED DATA


# In[61]:


df.to_csv("cleaned_products.csv",index=False)


# In[32]:


#CONFIRMATION MESSAGE


# In[62]:


print("Data cleaned successfully!")


# In[ ]:





# In[ ]:




