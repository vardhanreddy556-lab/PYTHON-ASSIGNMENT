#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd

df = pd.read_csv("clean_products.csv")

print(df.head())


# In[22]:


df.columns


# In[19]:


import pyodbc

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=VISHNU-PC\\SQLEXPRESS;"
    "DATABASE=master;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()
print("Connected Successfully")


# In[14]:


cursor.execute("""
IF DB_ID('ProductDB') IS NULL
    CREATE DATABASE ProductDB
""")

conn.commit()
print("ProductDB created successfully.")


# In[24]:


import pyodbc

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=VISHNU-PC\\SQLEXPRESS;"
    "DATABASE=ProductDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()
print("Connected to ProductDB successfully.")


# In[ ]:


#INSERT THE CLEANED DATAFRAME INTO TABLE


# In[26]:


df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df["discount"] = pd.to_numeric(df["discount"], errors="coerce")

df = df.fillna(0)


# In[27]:


for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO Products
        (ProductID, ProductName, Category, Price, Rating, Discount)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
    index + 1,
    str(row["Product Name"]),
    str(row["Category"]),
    row["Price"],
    row["Rating"],
    row["discount"]
    )

conn.commit()
print("Data inserted successfully.")


# In[ ]:




