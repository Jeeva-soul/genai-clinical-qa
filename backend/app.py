from fastapi import FastAPI
from backend.document_loader import load_documents, split_into_chunks
from backend.embedding_store import create_vectorstore
from backend.qa_engine import ask_question

app = FastAPI()

# Load documents and create vector index at startup
documents = load_documents("data/clinical_docs")
chunks = split_into_chunks(documents)
index, vectors, chunks = create_vectorstore(chunks)

@app.get("/ask")
def ask(q: str):
    answer = ask_question(q, index, vectors, chunks)
    return {"question": q, "answer": answer}

