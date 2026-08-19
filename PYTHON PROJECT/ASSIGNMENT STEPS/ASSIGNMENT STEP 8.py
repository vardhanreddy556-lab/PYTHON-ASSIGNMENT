#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df = pd.read_csv("clean_products.csv")


# In[5]:


df.to_csv("clean_products.csv", index=False)
print("clean_products.csv saved successfully.")


# In[ ]:


#ANALYSIS_SUMMARY.TEXT


# In[6]:


with open("analysis_summary.txt", "w") as file:
    file.write("PRODUCT ANALYSIS SUMMARY\n")
    file.write("=" * 40 + "\n\n")

    file.write(f"Total Products : {len(df)}\n")
    file.write(f"Average Price  : {df['Price'].mean():.2f}\n")
    file.write(f"Highest Price  : {df['Price'].max():.2f}\n")
    file.write(f"Lowest Price   : {df['Price'].min():.2f}\n")
    file.write(f"Average Rating : {df['Rating'].mean():.2f}\n\n")

    file.write("Products per Category:\n")
    file.write(df["Category"].value_counts().to_string())

print("analysis_summary.txt created successfully.")


# In[ ]:




