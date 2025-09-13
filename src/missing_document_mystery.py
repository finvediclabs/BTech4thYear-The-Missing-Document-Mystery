"""
The Missing Document Mystery
Theme: MongoDB CRUD & Indexing
Description: Simulates a bug with slow MongoDB search and missing documents.
"""

import pymongo
from pymongo import MongoClient
import time

# MongoDB connection (update URI as needed)
client = MongoClient('mongodb://localhost:27017/')
db = client['missing_document_db']
collection = db['documents']

def setup_documents():
    """Insert sample documents, some with missing fields."""
    collection.delete_many({})
    docs = [
        {"title": "Doc1", "content": "This is the first document."},
        {"title": "Doc2", "content": "Second document here."},
        {"title": "Doc3"},  # Missing 'content'
        {"title": "Doc4", "content": "Fourth document."},
        {"title": "Doc5", "content": "Fifth document."},
    ]
    collection.insert_many(docs)
    print("Inserted sample documents.")

def slow_search(keyword):
    """Simulate slow search due to missing index and missing documents."""
    start = time.time()
    results = list(collection.find({"content": {"$regex": keyword}}))
    end = time.time()
    print(f"Search took {end - start:.3f} seconds. Found {len(results)} documents.")
    for doc in results:
        print(doc)

def fix_index():
    """Create index to speed up search."""
    collection.create_index("content")
    print("Index created on 'content'.")

def fix_missing_docs():
    """Find and fix documents missing 'content'."""
    missing = list(collection.find({"content": {"$exists": False}}))
    for doc in missing:
        collection.update_one({"_id": doc["_id"]}, {"$set": {"content": "[Missing content]"}})
    print(f"Fixed {len(missing)} missing documents.")

if __name__ == "__main__":
    setup_documents()
    print("--- Buggy Search ---")
    slow_search("document")
    print("\n--- Fixing Index ---")
    fix_index()
    slow_search("document")
    print("\n--- Fixing Missing Documents ---")
    fix_missing_docs()
    slow_search("document")
