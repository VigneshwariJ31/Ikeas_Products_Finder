from flask import Flask, render_template, jsonify, request
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Connect to Elasticsearch
es = Elasticsearch('https://localhost:9200', basic_auth=('elastic', 'uRmY*oulxBA8+N4m_4nW'), verify_certs=False)

# Function to get products from Elasticsearch based on category
def get_products_from_es(category):
    try:
        query = {
            "query": {
                "match": {
                    "category": category
                }
            },
            "size": 1000
        }
        response = es.search(index="ikea_products", body=query)
        hits = response.get("hits", {}).get("hits", [])
        products = []

        for hit in hits:
            product = hit["_source"]
            products.append({
                "name": product.get("name"),
                "price": product.get("price"),
                "sellable_online": product.get("sellable_online"),
                "link": product.get("link"),
                "short_description": product.get("short_description"),
                "depth": product.get("depth"),
                "height": product.get("height")
            })

        return products
    except Exception as e:
        print(f"Error querying Elasticsearch: {e}")
        return None

# Function to search products by keyword
def search_products_by_keyword(keyword):
    try:
        query = {
            "query": {
                "multi_match": {
                    "query": keyword,
                    "fields": ["name", "category", "short_description", "designer", "link"],
                    "fuzziness": "AUTO"
                }
            },
            "size": 1000
        }
        response = es.search(index="ikea_products", body=query)
        hits = response.get("hits", {}).get("hits", [])
        products = []

        for hit in hits:
            product = hit["_source"]
            products.append({
                "name": product.get("name"),
                "price": product.get("price"),
                "sellable_online": product.get("sellable_online"),
                "link": product.get("link"),
                "short_description": product.get("short_description"),
                "depth": product.get("depth"),
                "height": product.get("height")
            })

        return products
    except Exception as e:
        print(f"Error querying Elasticsearch: {e}")
        return None

@app.route("/")
def index():
    return render_template("ikea_ui.html")

@app.route("/get_products/<category>")
def get_products(category):
    products = get_products_from_es(category)
    if products:
        return jsonify(products)
    return jsonify([])

@app.route("/search_products")
def search_products():
    keyword = request.args.get("keyword")
    if keyword:
        products = search_products_by_keyword(keyword)
        if products:
            return jsonify(products)
    return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)
