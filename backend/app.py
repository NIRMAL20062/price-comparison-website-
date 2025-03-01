from flask import Flask, jsonify, request  # Remove 'jsonifye'
from scraper import scrape_amazon, scrape_flipkart, scrape_ebay, get_price_history
import pandas as pd

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def search():
    product_name = request.args.get("product")
    if not product_name:
        return jsonify({"error": "Product name is required"}), 400
    
    amazon_results = scrape_amazon(product_name)
    flipkart_results = scrape_flipkart(product_name)
    ebay_results = scrape_ebay(product_name)
    
    all_results = amazon_results + flipkart_results + ebay_results
    return jsonify(all_results)

@app.route("/price-history", methods=["GET"])
def price_history():
    product_name = request.args.get("product")
    if not product_name:
        return jsonify({"error": "Product name is required"}), 400
    
    history = get_price_history(product_name)
    return jsonify(history.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)