import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set the number of rows and date range
num_rows = 1000
date_range = 30

# Set the regions, products, and product categories
regions = ['USA', 'Canada', 'UK', 'Mexico']
products = {'Kitchen': ['Microwave', 'Kettle', 'Toaster', 'Nespresso Machine', 'Dishwasher'],
            'Garden': ['Hose', 'Outdoor Chair', 'Hammock', 'Outdoor Table'],
            'Electronics': ['PS5', 'UHD TV', 'GoPro', 'Hairdryer'],
            'Bathroom': ['Shampoo', 'Candles', 'Handsoap', 'Bath Bomb']}

# Set the cost prices for each product
cost_prices = {'Microwave': 50, 'Kettle': 20, 'Toaster': 30, 'Nespresso Machine': 100, 
               'Dishwasher': 200, 'Hose': 10, 'Outdoor Chair': 40, 'Hammock': 60,
               'Outdoor Table': 80, 'PS5': 400, 'UHD TV': 500, 'GoPro': 300,
               'Hairdryer': 30, 'Shampoo': 5, 'Candles': 10, 'Handsoap': 3,
               'Bath Bomb': 4}

# Create the DataFrame
df = pd.DataFrame(columns=['Date', 'Region', 'Product Category', 
                           'Product', 'Sale Value', 'Cost Price'])

# Create the DataFrame
df = pd.DataFrame(columns=['Date', 'Region', 'Product Category', 
                           'Product', 'Sale Value', 'Cost Price'])

# Populate the DataFrame with random data
for i in range(num_rows):
    # Generate a random date within the last date_range days
    date = (datetime.now() - timedelta(days=np.random.randint(date_range))).strftime('%Y-%m-%d')
    
    # Choose a random region
    region = np.random.choice(regions)
    
    # Choose a random product category and product
    product_category = np.random.choice(list(products.keys()))
    product = np.random.choice(products[product_category])
    
    # Get the cost price of the product
    cost_price = cost_prices[product]
    
    # Generate a random sale value that is at least as high as the cost price
    sale_value = round(np.random.uniform(cost_price, cost_price * 1.5), 2)
    
    # Add the data to the DataFrame
    df.loc[i] = [date, region, product_category, product, sale_value, cost_price]

# Display the resulting DataFrame
print(df)

#Choose an appropriate location to store your data in an excel file:
df.to_excel('....\\data.xlsx')
