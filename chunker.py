def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end - overlap
    return chunks

def chunk_file(filepath):
    with open(filepath, "r") as f:
        text = f.read()
    
    # Split by blank lines (each review is its own chunk)
    chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
    return chunks

# Test on one file first
import os

all_chunks = []
files = [f for f in os.listdir(".") if f.endswith(".txt")]

for file in files:
    chunks = chunk_file(file)
    for chunk in chunks:
        all_chunks.append({"text": chunk, "source": file})

print(f"Total chunks: {len(all_chunks)}")

import random
sample = random.sample(all_chunks, 5)
for i, chunk in enumerate(sample):
    print(f"\n--- Sample {i+1} ({chunk['source']}) ---")
    print(chunk['text'])