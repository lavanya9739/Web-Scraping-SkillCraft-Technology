import requests
from bs4 import BeautifulSoup
import pandas as pd
import time  


base_url = "https://www.amazon.in/s?bbn=976389031&rh=n%3A976389031%2Cp_85%3A10440599031&page="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Empty lists to store the scraped data
product_names = []
prices = []
ratings = []

# Initialize page count and product count
page = 1
min_products = 30  # Set minimum number of products to scrape

# Loop until we have at least 30 products
while len(product_names) < min_products:
    url = base_url + str(page)
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page}: {e}")
        break

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all product containers
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    
    # Extract name, price, and rating for each product
    for product in products:
        if len(product_names) >= min_products:  # Stop if we reach 30 products
            break
        
        try:
            # Product name
            name = product.h2.text.strip() if product.h2 else "N/A"
            
            # Product price
            price = product.find('span', class_='a-price-whole')
            price = f"₹{price.text.strip()}" if price else "N/A"
            
            # Product rating
            rating = product.find('span', class_='a-icon-alt')
            rating = rating.text.strip() if rating else "N/A"
            
            # Append data to lists
            product_names.append(name)
            prices.append(price)
            ratings.append(rating)
        
        except Exception as e:
            print(f"Error processing product: {e}")
            continue
    
    # Move to the next page
    page += 1
    
    # Add delay between requests to avoid blocking
    time.sleep(2)

# Save the data into a CSV file
df = pd.DataFrame({'Product Name': product_names, 'Price': prices, 'Rating': ratings})
df.to_csv('amazon_products_books.csv', index=False)

# Print the DataFrame
print(df)
