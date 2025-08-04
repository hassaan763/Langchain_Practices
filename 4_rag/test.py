import os
from langchain_chroma import Chroma
from langchain_together import TogetherEmbeddings

# Define your persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

# Load the embedding function
embeddings = TogetherEmbeddings(model="BAAI/bge-base-en-v1.5")

# Load the Chroma DB
db = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)

# Fetch all documents stored in the DB
data = db.get()

# Print how many documents were stored
print(f"Number of documents stored: {len(data['documents'])}")

# Show sample content
for i, doc in enumerate(data["documents"][:3], 1):  # show first 3 chunks
    print(f"\n--- Document Chunk {i} ---")
    print(doc)
