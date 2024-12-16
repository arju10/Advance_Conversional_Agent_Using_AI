import os
import chromadb
from chromadb.config import Settings

# Set the path for persistent storage
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "/media/arju/New Volume/File-8/All Projects/Advance_Conversional_Agent_Using_AI/chromadb")

def handle_query(user_query, context):
    # Initialize the client using the updated API
    client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",  # Backend for ChromaDB
        persist_directory=CHROMA_DB_PATH  # Path for persistence
    ))

    # Access the collection
    collection_name = "conversional_agent_db"
    collection = client.get_or_create_collection(collection_name)

    # Perform the query
    results = collection.query(query_texts=[user_query], n_results=1)
    return results["documents"][0] if results and results["documents"] else "I couldn't find an answer to your query."
