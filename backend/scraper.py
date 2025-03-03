import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_amazon(product_name):
    url = f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all("div", {"data-component-type": "s-search-result"})
    
    results = []
    for item in items:
        title = item.find("h2").text.strip()
        price = item.find("span", {"class": "a-price-whole"})
        if price:
            price = price.text.strip().replace(",", "")
        else:
            price = "N/A"
        results.append({"title": title, "price": price, "source": "Amazon"})
    return results

def scrape_flipkart(product_name):
    url = f"https://www.flipkart.com/search?q={product_name.replace(' ', '%20')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all("div", {"class": "_1AtVbE"})
    
    results = []
    for item in items:
        title = item.find("div", {"class": "_4rR01T"})
        if title:
            title = title.text.strip()
        price = item.find("div", {"class": "_30jeq3"})
        if price:
            price = price.text.strip().replace("₹", "").replace(",", "")
        else:
            price = "N/A"
        results.append({"title": title, "price": price, "source": "Flipkart"})
    return results

def scrape_ebay(product_name):
    url = f"https://www.ebay.com/sch/i.html?_nkw={product_name.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all("div", {"class": "s-item__info"})
    
    results = []
    for item in items:
        title = item.find("h3", {"class": "s-item__title"})
        if title:
            title = title.text.strip()
        price = item.find("span", {"class": "s-item__price"})
        if price:
            price = price.text.strip().replace("$", "").replace(",", "")
        else:
            price = "N/A"
        results.append({"title": title, "price": price, "source": "eBay"})
    return results

def scrape_all(product_name):
    amazon_results = scrape_amazon(product_name)
    flipkart_results = scrape_flipkart(product_name)
    ebay_results = scrape_ebay(product_name)
    all_results = amazon_results + flipkart_results + ebay_results
    return all_results