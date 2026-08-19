#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np


# In[ ]:


#LOAD THE CLEANED DATA


# In[24]:


df = pd.read_csv("cleaned_products.csv")


# In[17]:


print(df["Rating"].unique())


# In[ ]:


#CONVERT RATING TO NUMBERS


# In[25]:


rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)


# In[ ]:


#CHECK THE DATA


# In[30]:


print(df.head())
print(df.info())


# In[ ]:


#CALCULATE STATISTICS


# In[31]:


print("Average Price:", df["Price"].mean())
print("Maximum Price:", df["Price"].max())
print("Minimum Price:", df["Price"].min())
print("Average Rating:", df["Rating"].mean())


# In[ ]:


#GROUP THE DATA


# In[32]:


category_summary = df.groupby("Category").agg({
    "Price": "mean",
    "Rating": "mean"
})
print(category_summary)


# In[ ]:


#CREATE NEW COLUMNS


# In[33]:


#PRICE CATEGORY
df["Price Category"] = df["Price"].apply(
    lambda x: "High" if x >= 50 else "Low"
)


# In[13]:


#AVALIABILITY 
df["Availability Status"] = df["Availability"].apply(
    lambda x: "Available" if "In stock" in x else "Out of Stock"
)


# In[ ]:


#USE NUMPY FUNCTIONS


# In[14]:


df["Price_Level"] = np.where(df["Price"] > 5000, "High", "Low")


# In[ ]:


#DEMONSTRATE VECTORIZED OPERATIONS


# In[27]:


df["Price_INR"] = df["Price"] * 115


# In[ ]:


#MISSING VALUE HANDILING


# In[34]:


print(df.isnull().sum())


# In[ ]:


#SAVE THE ANALYSIS


# In[35]:


df.to_csv("analyzed_products.csv",index=False)


# In[18]:


#remove rating score column
df = df.drop("Rating Score", axis=1)


# In[20]:


#remove price_level column
df.drop("Price_Level", axis=1,inplace=True)


# In[36]:


df.columns


# In[ ]:




