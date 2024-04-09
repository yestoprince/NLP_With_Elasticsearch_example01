# NLP text search using hugging face transformer model

# Required libraries 
from elasticsearch import Elasticsearch
from getpass import getpass
from urllib.request import urlopen
import json
from time import sleep
import pandas as pd


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


dataset = pd.read_csv("/Users/prince/Documents/Python Workspace/VectorSearchExamples/myntra_dataset.csv")
#print(dataset.head())
dataset.fillna("None", inplace=True)
#print(dataset.columns)

# List of columns to keep
columns_to_keep = ['URL', 'Description']

# Create a new DataFrame with only the specified columns
new_df = dataset[columns_to_keep].copy()

# Display the new DataFrame

#print(new_df.head())

# Create an ingest pipeline in Elasticsearch 

# ingest pipeline definition

es.ingest.put_pipeline(
    id=PIPELINE_ID,
    processors=[
        {
            "inference": {
                "model_id": PIPELINE_ID,
                "target_field": "description_embedding",
                "field_map": {"Description": "text_field"},
            }
        }
    ],
)


# Code snippet 
# PUT _ingest/pipeline/vectorise_ecomm_myntra
# {
#   "processors": [
#     {
#       "inference": {
#         "model_id": "sentence-transformers__all-mpnet-base-v2",
#         "target_field": "description_embeddings",
#         "field_map": {
#           "Description": "text_field"
#         }
#       }
#     }
#   ]
# }

# Now next is index mapping, index settings, creating index


from indexmapping import indexMapping
print(indexMapping)

#es.indices.create(index="myntra_products", mappings=indexMapping)

INDEX_SETTINGS = {
    "index": {
        "number_of_replicas": "1",
        "number_of_shards": "1",
        "default_pipeline": PIPELINE_ID,
    }
}

# check if we want to delete index before creating the index
if SHOULD_DELETE_INDEX:
    if es.indices.exists(index=INDEX_NAME):
        print("Deleting existing %s" % INDEX_NAME)
        es.indices.delete(index=INDEX_NAME, ignore=[400, 404])

print("Creating index %s" % INDEX_NAME)
es.indices.create(
    index=INDEX_NAME, mappings=indexMapping, settings=INDEX_SETTINGS, ignore=[400, 404]
)

# Now index has been created with the settings and mapping 

# Now we need to ingest the data and pipeline will vectorize the required field.

# # Prepare actions for bulk indexing

# Function to format DataFrame row into Elasticsearch document format
def format_document(row):
    return {
        "_index": "myntra_products",  # Index name
        "_source": row.to_dict()  # Convert row to dictionary
    }

# Bulk indexing

# Define maximum number of rows to iterate
max_rows = 5

# Bulk indexing
actions = []
for _, row in new_df.head(1000).iterrows():
    actions.append({"index": {"_index": INDEX_NAME}})
    actions.append(row.to_dict())

response = es.bulk(index=INDEX_NAME, body=actions)

# Check response for errors
if response["errors"]:
    for item in response["items"]:
        if "index" in item and item["index"]["status"] != 201:
            print("Error indexing document:", item)
else:
    print("Bulk insert successful.")


