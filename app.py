from sentence_transformers import SentenceTransformer
import chromadb
from groq import Groq
import os
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

# Set up embedding model and ChromaDB
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.create_collection("stevens_reviews")

# Load and store all chunks
def chunk_file(filepath):
    with open(filepath, "r") as f:
        text = f.read()
    return [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

all_chunks = []
files = [f for f in os.listdir(".") if f.endswith(".txt")]
for file in files:
    for chunk in chunk_file(file):
        all_chunks.append({"text": chunk, "source": file})

texts = [c["text"] for c in all_chunks]
sources = [c["source"] for c in all_chunks]
embeddings = model.encode(texts).tolist()
collection.add(
    documents=texts,
    embeddings=embeddings,
    metadatas=[{"source": s} for s in sources],
    ids=[str(i) for i in range(len(texts))]
)

# Set up Groq
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask(question):
    # Retrieve relevant chunks
    query_embedding = model.encode([question]).tolist()
    results = collection.query(query_embeddings=query_embedding, n_results=5)
    
    chunks = results["documents"][0]
    chunk_sources = [m["source"] for m in results["metadatas"][0]]
    
    context = "\n\n".join(chunks)
    unique_sources = list(set(chunk_sources))
    
    # Generate grounded response
    prompt = f"""You are a helpful assistant for Stevens Institute of Technology students.
Answer the question using ONLY the information in the provided documents.
If the documents don't contain enough information to answer, say 'I don't have enough information on that.'
Always cite which source(s) your answer comes from.

Documents:
{context}

Question: {question}"""

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return {
        "answer": response.choices[0].message.content,
        "sources": unique_sources
    }

def handle_query(question):
    result = ask(question)
    sources = "\n".join(f"• {s}" for s in result["sources"])
    return result["answer"], sources

# Build Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Stevens Unofficial Guide")
    gr.Markdown("Ask questions about professors and courses at Stevens Institute of Technology.")
    inp = gr.Textbox(label="Your question")
    btn = gr.Button("Ask")
    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Retrieved from", lines=4)
    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])

demo.launch()