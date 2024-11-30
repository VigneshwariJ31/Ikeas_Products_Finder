import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# Load the IKEA data from a JSON file
with open(r'C:\Users\vicky\OneDrive\Desktop\ASU\Coursework\CSE 512\Extra Credit\ikea_products.json', 'r') as file:
    ikea_data = json.load(file)

# Connect to Elasticsearch
es = Elasticsearch('https://localhost:9200', basic_auth=('elastic', 'uRmY*oulxBA8+N4m_4nW'), verify_certs=False)

# Define the index name
index_name = "ikea_products"

# Create the index if it doesn't exist
if not es.indices.exists(index=index_name):
    es.indices.create(
        index=index_name,
        body={
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            },
            "mappings": {
                "properties": {
                    "item_id": {"type": "long"},
                    "name": {"type": "text"},
                    "category": {"type": "keyword"},
                    "price": {"type": "float"},
                    "sellable_online": {"type": "boolean"},
                    "link": {"type": "keyword"},
                    "short_description": {"type": "text"},
                    "designer": {"type": "text"},
                    "depth": {"type": "float"},
                    "height": {"type": "float"},
                    "width": {"type": "float"}
                }
            }
        }
    )

# Prepare data for bulk upload
actions = []
for item in ikea_data:
    action = {
        "_index": index_name,
        "_source": {
            "item_id": item["item_id"],
            "name": item["name"],
            "category": item["category"],
            "price": item["price"],
            "sellable_online": item["sellable_online"] == "True",  # Convert "True"/"False" to boolean
            "link": item["link"],
            "short_description": item["short_description"],
            "designer": item["designer"],
            "depth": item["depth"],
            "height": item["height"] if item["height"] else None,  # Handle empty height values
            "width": item["width"]
        },
    }
    actions.append(action)

# Upload the data to Elasticsearch
success, failed = 0, 0
try:
    # Upload the data without batching (i.e., regular upload)
    success, failed = bulk(es, actions, stats_only=False, raise_on_error=True)
    print(f"Successfully uploaded {success} documents.")
except Exception as e:
    print(f"Error during bulk upload: {e}")
