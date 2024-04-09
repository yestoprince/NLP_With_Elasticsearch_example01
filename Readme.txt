Documentation for NLP_Model_Deployement_Indexing.py:
Introduction:
This script is designed to deploy an NLP text search system using a Hugging Face Transformer model. It utilizes Elasticsearch for indexing and searching text data.
Requirements:
Python 3.x
elasticsearch library (pip install elasticsearch)
pandas library (pip install pandas)
Configuration:
PIPELINE_ID: Identifier for the pipeline used in Elasticsearch.
INDEX_NAME: Name of the Elasticsearch index.
SHOULD_DELETE_INDEX: Boolean flag to determine whether to delete the existing index before creating a new one.
ELASTIC_CLOUD_ID: Cloud ID for Elasticsearch (sensitive information).
ELASTIC_API_KEY: API key for Elasticsearch (sensitive information).
Steps:
Connects to Elasticsearch using provided credentials.
Reads data from a CSV file (myntra_dataset.csv) containing product information.
Creates an ingest pipeline in Elasticsearch to vectorize text data.
Defines index mapping for Elasticsearch.
Creates or updates the Elasticsearch index with the specified mapping and settings.
Indexes product data into Elasticsearch.
Documentation for QueryModel.py:
Introduction:
This script queries the Elasticsearch index created by NLP_Model_Deployement_Indexing.py to perform text searches using a Hugging Face Transformer model.
Requirements:
Python 3.x
elasticsearch library (pip install elasticsearch)
Configuration:
PIPELINE_ID: Identifier for the pipeline used in Elasticsearch.
INDEX_NAME: Name of the Elasticsearch index.
ELASTIC_CLOUD_ID: Cloud ID for Elasticsearch (sensitive information).
ELASTIC_API_KEY: API key for Elasticsearch (sensitive information).
Steps:
Connects to Elasticsearch using provided credentials.
Constructs a query using a Hugging Face Transformer model to search for similar text.
Executes the query on the Elasticsearch index.
Displays search results including descriptions and URLs.
Note:
Sensitive information such as ELASTIC_CLOUD_ID and ELASTIC_API_KEY have been obscured with asterisks (*********). Make sure to replace them with actual credentials when running the code.

Ensure that proper error handling and exception catching are implemented throughout the code for robustness.

Documentation for indexmapping.py:
Introduction:
This module defines the index mapping for Elasticsearch used in the indexing process.
Contents:
indexMapping: Dictionary defining the mapping schema for Elasticsearch index.
Index Mapping:
URL: Text field mapping for product URLs.
Description: Text field mapping for product descriptions.
description_embedding: Nested property containing the embedding of product descriptions.
is_truncated: Boolean field indicating whether the description is truncated.
model_id: Text field mapping for the ID of the embedding model used.
predicted_value: Dense vector field containing the embedding of the description with specified dimensions and similarity metric.
Note:
Ensure that the index mapping defined in indexmapping.py matches the actual structure of your Elasticsearch index. Modify it accordingly if your index schema differs.