#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


#CHOOSE A WEBSITE


# In[3]:


url = "https://books.toscrape.com/"


# In[4]:


#DOWNLOAD THE WEBPAGE


# In[5]:


response = requests.get(url)
print(response.status_code)


# In[6]:


#READ THE HTML


# In[7]:


soup = BeautifulSoup(response.text,"html.parser")


# In[8]:


#CHECK THE PAGE TITLE


# In[9]:


print(soup.title.text)


# In[2]:


import requests
from bs4 import BeautifulSoup

data = []

for page in range(1, 9):   # Pages 1 to 8
    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("article", class_="product_pod")

    for product in products:
        name = product.h3.a["title"]
        price = product.find("p", class_="price_color").text
        rating = product.find("p")["class"][1]
        availability = product.find("p", class_="instock availability").get_text(strip=True)
        product_url = "https://books.toscrape.com/catalogue/" + product.h3.a["href"]

        data.append([name, price, rating, availability, product_url])

# Keep only the first 150 books
data = data[:150]


# In[4]:


print(len(data))


# In[14]:


#STORE THE DATA IN A LIST


# In[15]:


data = []

for product in products:
    name = product.h3.a["title"]
    price = product.find("p",class_="price_color").text
    rating = product.find("p")["class"][1]

    data.append([name, price, rating])


# In[16]:


#CREATE A DATA FRAME


# In[8]:


df = pd.DataFrame(
    data,
    columns=[
        "Product Name",
        "Price",
        "Rating",
        "Availability",
        "Product URL"
    ]
)

print(df.shape)


# In[11]:


df["Reviews"] = 0
df["discount"] = 0


# In[18]:


#DISPLAY THE DATA


# In[12]:


print(df)


# In[20]:


#SAVE THE DATA TO A CSV FILE


# In[13]:


df.to_csv("raw_products.csv",index=False)
print("Data saved successfully!")


# In[ ]:




