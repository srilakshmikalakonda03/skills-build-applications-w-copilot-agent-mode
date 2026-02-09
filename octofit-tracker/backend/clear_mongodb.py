#!/usr/bin/env python
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['octofit_db']

# Drop all collections
for collection_name in db.list_collection_names():
    db[collection_name].drop()
    print(f"Dropped collection: {collection_name}")

print("✅ MongoDB database cleared successfully!")
client.close()
