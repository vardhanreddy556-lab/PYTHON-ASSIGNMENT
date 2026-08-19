#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#SCRAPER CLASS


# In[21]:


import requests
from bs4 import BeautifulSoup

class Scraper:

    website = "https://books.toscrape.com"

    def __init__(self):
        self.data = []

    def scrape_data(self):

        self.data = []

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

                self.data.append([
                    name,
                    price,
                    rating,
                    availability,
                    product_url
                ])

        self.data = self.data[:150]

        return self.data


# In[ ]:


#DATA PROCESSOR CLASS


# In[39]:


import pandas as pd

class DataProcessor:

    file_name = "clean_products.csv"

    def __init__(self, data):
        self.data = data

    def clean_data(self):

        # Convert list to DataFrame
        self.data = pd.DataFrame(
            self.data,
            columns=[
                "Product Name",
                "Price",
                "Rating",
                "Availability",
                "Product URL"
            ]
        )

        # Add missing columns
        self.data["Reviews"] = 0
        self.data["discount"] = 0

        # Add Category column
        self.data["Category"] = "Books"

        # Remove duplicates
        self.data = self.data.drop_duplicates()

        # Remove missing values
        self.data = self.data.dropna()

        # Clean Price column
        self.data["Price"] = self.data["Price"].astype(str)
        self.data["Price"] = self.data["Price"].str.replace("Â£", "", regex=False)
        self.data["Price"] = self.data["Price"].str.replace("£", "", regex=False)
        self.data["Price"] = self.data["Price"].astype(float)

        # Convert Rating to numbers
        rating_map = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }

        self.data["Rating"] = self.data["Rating"].map(rating_map)

        return self.data

    def process_data(self):
        self.data.to_csv(self.file_name, index=False)
        print("Data cleaned successfully!")

    def save_clean_data(self):
        self.data.to_csv(self.file_name, index=False)


# In[ ]:


#ANALYZER VISUALIZER CLASS


# In[40]:


import matplotlib.pyplot as plt
import plotly.express as px

class AnalyzerVisualizer:

    report_name = "analysis_summary.txt"

    def __init__(self, data):
        self.data = data

    def analyze_data(self):

        print("Average Price:", self.data["Price"].mean())
        print("Highest Price:", self.data["Price"].max())
        print("Lowest Price:", self.data["Price"].min())

    def create_charts(self):

        # 1. Bar Chart - Average Price by Category
        avg_price = self.data.groupby("Category")["Price"].mean()

        plt.figure(figsize=(8,5))
        avg_price.plot(kind="bar")
        plt.title("Average Price by Category")
        plt.xlabel("Category")
        plt.ylabel("Average Price")
        plt.tight_layout()
        plt.savefig("average_price_category.png")
        plt.show()

        # 2. Histogram - Product Ratings
        plt.figure(figsize=(8,5))
        self.data["Rating"].hist()
        plt.title("Product Ratings")
        plt.xlabel("Rating")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig("rating_histogram.png")
        plt.show()

        # 3. Scatter Plot - Price vs Rating
        fig = px.scatter(
            self.data,
            x="Price",
            y="Rating",
            title="Price vs Rating"
        )
        fig.write_html("price_vs_rating.html")
        fig.show()

    def save_report(self):

        with open(self.report_name, "w") as f:
            f.write("Product Analysis Report\n")
            f.write(f"Average Price: {self.data['Price'].mean()}\n")
            f.write(f"Highest Price: {self.data['Price'].max()}\n")
            f.write(f"Lowest Price: {self.data['Price'].min()}\n")

        print("Report saved successfully!")


# In[ ]:


#MAIN PROGRAM


# In[41]:


scraper = Scraper()
raw_data = scraper.scrape_data()

processor = DataProcessor(raw_data)
processor.clean_data()

print(processor.data.head())
print(processor.data.columns)

analyzer = AnalyzerVisualizer(processor.data)
analyzer.analyze_data()
analyzer.create_charts()


# In[51]:


analyzer.create_charts()


# In[45]:


processor.clean_data()
processor.process_data()


# In[ ]:




