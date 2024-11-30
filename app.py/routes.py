from flask import render_template, request
from app import app
from elasticsearch import Elasticsearch

# Initialize Elasticsearch
es = Elasticsearch(
    hosts=["http://localhost:9200"],
    basic_auth=("elastic", "uRmY*oulxBA8+N4m_4nW"),
    verify_certs=False,
)

@app.route("/")
def index():
    return render_template("ikea_ui.html")

@app.route("/search", methods=["POST"])
def search():
    # Logic for search (copy from app.py)
    pass
