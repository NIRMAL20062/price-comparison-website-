from flask import Flask, render_template, request, jsonify
from scraper import scrape_all
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    product_name = request.form.get("product_name")
    results = scrape_all(product_name)
    return jsonify(results)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)