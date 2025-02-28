import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_amazon(product_name):
    url = f"https://www.amazon.com/s?k={product_name.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("div", {"data-component-type": "s-search-result"})
    
    results = []
    for item in items:
        name = item.find("span", class_="a-text-normal").text.strip()
        price = item.find("span", class_="a-offscreen")
        price = price.text.strip() if price else "N/A"
        results.append({"Website": "Amazon", "Product": name, "Price": price})
    
    return results

def scrape_flipkart(product_name):
    url = f"https://www.flipkart.com/search?q={product_name.replace(' ', '%20')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("div", {"class": "_1AtVbE"})
    
    results = []
    for item in items:
        name = item.find("div", {"class": "_4rR01T"})
        price = item.find("div", {"class": "_30jeq3"})
        if name and price:
            results.append({"Website": "Flipkart", "Product": name.text.strip(), "Price": price.text.strip()})
    
    return results

def scrape_ebay(product_name):
    url = f"https://www.ebay.com/sch/i.html?_nkw={product_name.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("div", {"class": "s-item__info"})
    
    results = []
    for item in items:
        name = item.find("h3", {"class": "s-item__title"})
        price = item.find("span", {"class": "s-item__price"})
        if name and price:
            results.append({"Website": "eBay", "Product": name.text.strip(), "Price": price.text.strip()})
    
    return results

def get_price_history(product_name):
    # Simulate price history (replace with actual scraping logic)
    data = {
        "Date": ["2023-10-01", "2023-10-02", "2023-10-03"],
        "Price": [100, 95, 90]
    }
    return pd.DataFrame(data)