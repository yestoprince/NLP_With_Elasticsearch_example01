# NLP text search using hugging face transformer model

# Required libraries 
from elasticsearch import Elasticsearch
from getpass import getpass
from urllib.request import urlopen
import json
from time import sleep


#PIPELINE_ID = "sentence-transformers__all-mpnet-base-v2"
PIPELINE_ID = "sentence-transformers__all-minilm-l6-v2"
INDEX_NAME = "myntra_products"
SHOULD_DELETE_INDEX = True

ELASTIC_CLOUD_ID = getpass("Elastic Cloud ID: ")
# https://www.elastic.co/search-labs/tutorials/install-elasticsearch/elastic-cloud#creating-an-api-key
ELASTIC_API_KEY = getpass("Elastic Api Key: ")

es = Elasticsearch(
    cloud_id=ELASTIC_CLOUD_ID, api_key=ELASTIC_API_KEY, request_timeout=600
)

if es.ping():
    print("You are connected to below cluster => \n=====================================")
    #print(es.info())  
else:
    print("Couldn't connect to ES Cluster")


source_fields = ["URL", "Description"]

query = {
    "field": "description_embedding.predicted_value",
    "k": 5,
    "num_candidates": 50,
    "query_vector_builder": {
        "text_embedding": {
            "model_id": "sentence-transformers__all-minilm-l6-v2",
            "model_text": "skinny fit jeans",
        }
    },
}

response = es.search(index=INDEX_NAME, fields=source_fields, knn=query, source=False)


def show_results(results):
    for result in results:
        print(f'Description: {result["fields"]["Description"]}')
        print(f'URL: {result["fields"]["URL"]}')
        print(f'Score: {result["_score"]}\n')


show_results(response.body["hits"]["hits"])