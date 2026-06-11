from sentence_transformers import SentenceTransformer
import chromadb
import os

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Set up ChromaDB
client = chromadb.Client()
collection = client.create_collection("stevens_reviews")

# Load all chunks from chunker.py
def chunk_file(filepath):
    with open(filepath, "r") as f:
        text = f.read()
    chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
    return chunks

all_chunks = []
files = [f for f in os.listdir(".") if f.endswith(".txt")]
for file in files:
    chunks = chunk_file(file)
    for chunk in chunks:
        all_chunks.append({"text": chunk, "source": file})

# Embed and store in ChromaDB
texts = [c["text"] for c in all_chunks]
sources = [c["source"] for c in all_chunks]
embeddings = model.encode(texts).tolist()

collection.add(
    documents=texts,
    embeddings=embeddings,
    metadatas=[{"source": s} for s in sources],
    ids=[str(i) for i in range(len(texts))]
)

print(f"Stored {len(texts)} chunks in ChromaDB")


def retrieve(query, k=5):
    query_embedding = model.encode([query]).tolist()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=k
    )
    for i, (doc, meta, dist) in enumerate(zip(results["documents"][0], results["metadatas"][0], results["distances"][0])):
        print(f"\n--- Result {i+1} (source: {meta['source']}, distance: {dist:.2f}) ---")
        print(doc)

# Test with one of your evaluation questions
retrieve("What do students say about Jacek's exams?")

retrieve("Is Professor Akum good for CS115?")
retrieve("What do students think about the Stevens CS program?")