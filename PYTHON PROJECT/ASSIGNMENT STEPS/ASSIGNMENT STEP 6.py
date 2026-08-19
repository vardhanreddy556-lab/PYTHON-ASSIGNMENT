#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
df = pd.read_csv("clean_products.csv")


# In[12]:


import matplotlib.pyplot as plt


# In[ ]:


#BAR CHART (MATPLOTLIB)


# In[13]:


avg_price = df.groupby("Category")["Price"].mean()

plt.figure(figsize=(8,5))
avg_price.plot(kind="bar")
plt.title("Average Price per Category")
plt.xlabel("Category")
plt.ylabel("Average Price")
plt.tight_layout()
plt.savefig("average_price_bar.png")
plt.show()


# In[9]:


type(df)


# In[ ]:


#HISTOGRAM (MATPLOTLIB)


# In[32]:


plt.figure(figsize=(8,5))
plt.hist(df["Rating"], bins=10)
plt.title("Product Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("ratings_histogram.png")
plt.show()


# In[30]:


import pandas as pd

df = pd.read_csv("analyzed_products.csv")


# In[31]:


print(df["Rating"].head())


# In[ ]:


#INTERACTIVE SCATTER PLOT (PLOTLY)


# In[41]:


import plotly.express as px

fig = px.scatter(
    df,
    x="Price",
    y="Rating",
    color="Category",
    hover_data=["Product Name"],
    title="Price vs Rating"
)

fig.write_html("price_vs_rating.html")
fig.show()


# In[ ]:




