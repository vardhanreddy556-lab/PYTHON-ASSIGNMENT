#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#STRING,LIST,AND DICTIONARY OPERATIONS


# In[ ]:


#READ THE CLEANED CSV


# In[100]:


import pandas as pd
df = pd.read_csv("cleaned_products.csv")


# In[63]:


print(df.head())


# In[22]:


#ADD CATEGORIES


# In[101]:


df["Category"] = "Books"


# In[24]:


#ADD PRODUCT ID


# In[102]:


df["Product ID"] = ["P" + str(i+1).zfill(3) for i in range(len(df))]


# In[26]:


#CLEAN PRODUCT NAMES


# In[103]:


df["Product Nmae"] = df["Product Name"].str.strip()
df["Product Name"] = df["Product Name"].str.title()


# In[28]:


#STRING REPLACEMENT


# In[104]:


df["Product Name"] = df["Product Name"].str.replace("-", " ")


# In[30]:


#STRING SLICING


# In[105]:


df["short Name"] = df["Product Name"].str[:15]


# In[32]:


#LIST COMPREHENSION


# In[106]:


product_list = [name.strip().title() for name in df["Product Name"]]
print(product_list[:5])


# In[34]:


#CREATE TUPLES


# In[107]:


product_tuples = list(zip(
    df["Product ID"],
    df["Product Name"],
    df["Category"],
    df["Price"],
    df["Rating"]
))

print(product_tuples[:5])


# In[36]:


#CREATE A PRODUCT DICTIONARY


# In[108]:


Product_dict = {row["Product ID"]:
               (row["Product Name"],
                row["Category"],
                row["Price"],
                row["Rating"])
            for _, row in df.iterrows()
               }
print(Product_dict)



# In[ ]:


#CATEGORY COUNT DICTIONARY


# In[109]:


category_count = df["Category"].value_counts().to_dict()
print(category_count)


# In[ ]:


#CATEGORY PRICE LIST DICTIONARY


# In[110]:


category_price = df.groupby("Category")["Price"].apply(list).to_dict()
print(category_price)


# In[121]:


print("data cleaned successfully!")


# In[119]:


df.to_csv("cleaned_products.csv",index=False)


# In[120]:


df.head()


# In[117]:


print(df.columns.tolist())


# In[118]:


df.drop(columns=["short Name"],inplace=True)
df.drop(columns=["Product Nmae"],inplace=True)


# In[ ]:




