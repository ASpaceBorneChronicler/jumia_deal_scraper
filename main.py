import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.jumia.co.ke/flash-sales/"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

# Get all product cards on the flash page
product_cards = soup.find_all("article", {"class": "prd _fb _p col c-prd"})

product_list = {} # Empty list for product details

# Populate the product list with the products information in the div.info
for index, article in enumerate(product_cards):
    info_div = article.find('div', class_='info')
    if info_div: # Checks if there is a div.info
        # Extract information from within the div.info
        name = info_div.find('h3', class_='name').text if info_div.find('h3', class_='name') else 'N/A'
        price = info_div.find('div', class_='prc').text if info_div.find('div', class_='prc') else 'N/A'
        original_price = info_div.find('div', class_='s-prc-w').find('div',class_='old').text if info_div.find('div', class_='s-prc-w') else 'N/A'
        rating = info_div.find('div', class_='stars').text if info_div.find('div', class_='stars') else 'No rating'
        
        product_list[index]={
                                'name': name,
                                'price': price,
                                'old price':original_price,
                                'rating': rating,
                            }

# Make div and save it in a csv file
df = pd.DataFrame.from_dict(product_list, orient='index')
df.to_csv('jumia_flash_sales.csv', index=False)



        


