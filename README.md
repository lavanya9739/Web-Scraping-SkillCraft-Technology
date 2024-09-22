# Web-Scraping-SkillCraft-Technology
Create a program that extracts product information,such as names ,prices, and ratings, from an online e-commerce Website and stores the data in a structured format like a CSV file

This Python script scrapes product details such as name, price, and rating from the Books section on Amazon India. It collects data from multiple pages until it accumulates a minimum of 30 products. The data is then saved into a CSV file (amazon_products_books.csv) and displayed in a pandas DataFrame.

Requirements
The following Python libraries are required to run the script:

- requests – To send HTTP requests to Amazon's web pages.
- BeautifulSoup from the bs4 library – To parse the HTML content of the web pages.
- pandas – To store and manipulate the scraped data.
- time – To manage delays between requests.

Script Workflow
Initialization:

A base_url is defined for the Books section of Amazon India, specifying only Prime-eligible products.
A headers dictionary is set to mimic a browser request and avoid getting blocked by Amazon.
Scraping Loop:

The script loops through Amazon search result pages, starting from page 1. The loop continues until at least 30 products are scraped.
It fetches each page, parses the HTML using BeautifulSoup, and extracts the product's name, price, and rating.
If there is an issue with fetching or parsing, the error is handled, and the loop continues to the next page or product.
Data Storage:

The script collects the scraped data (product name, price, and rating) into lists.
Once the required number of products is gathered, the data is saved into a CSV file (amazon_products_books.csv) and printed as a DataFrame.
How to Use
Run the Script:

Simply run the script in a Python environment. It will start scraping books from Amazon.
The script continues fetching product details from subsequent pages until it has collected at least 30 products.
A delay of 2 seconds is added between each page request to avoid overwhelming the server.
CSV Output:

The collected data will be saved as a CSV file (amazon_products_books.csv) in the same directory where the script is run.
Error Handling:

If a page fails to load, the error message is displayed and the script moves to the next page.
If a product's name, price, or rating is missing, it is marked as "N/A".
Key Variables
- base_url: Base URL for the Books section on Amazon India (Prime-eligible products).
- headers: Dictionary mimicking a web browser to avoid request blocking.
- min_products: Minimum number of products to scrape, set to 30.
