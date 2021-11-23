from azure.cosmos import CosmosClient
import os

os.environ['ACCOUNT_URI']="https://megha16.documents.azure.com:443/"
os.environ['ACCOUNT_KEY']="njWynf2yVf65R01XXIYGAHkwF0w0imf8uDuqN4YncXnIJnJ1S6ZqFTV1ZL8sJI0e4rPXWzBKMEyEK0Ei8Ar0tw=="

url = os.environ['ACCOUNT_URI']
key = os.environ['ACCOUNT_KEY']
client = CosmosClient(url, credential=key)
database_name = 'testDatabase'
database = client.get_database_client(database_name)
container_name = 'smhproducts'
container = database.get_container_client(container_name)

# Enumerate the returned items
import json
for item in container.query_items(
        query='SELECT * FROM smhproducts r WHERE r.id="item3"',
        enable_cross_partition_query=True):
    print(json.dumps(item, indent=True))