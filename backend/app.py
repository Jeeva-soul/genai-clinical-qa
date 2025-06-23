from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from backend.qa_engine import ask_question
from backend.document_loader import load_documents, split_into_chunks, parse_pdf_to_chunks
from backend.embedding_store import create_vectorstore

app = FastAPI()

# Global state
index = None
vectors = None
chunks = None

class QuestionRequest(BaseModel):
    question: str

# Load default docs at startup
@app.on_event("startup")
def load_initial_documents():
    global index, vectors, chunks
    documents = load_documents("data/clinical_docs")
    chunks = split_into_chunks(documents)
    index, vectors, chunks = create_vectorstore(chunks)

@app.post("/ask")
def ask(req: QuestionRequest):
    return {
        "question": req.question,
        "answer": ask_question(req.question, index, vectors, chunks)
    }

@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    global index, vectors, chunks
    try:
        contents = await file.read()
        with open("uploaded_temp.pdf", "wb") as f:
            f.write(contents)

        new_chunks = parse_pdf_to_chunks("uploaded_temp.pdf")
        index, vectors, chunks = create_vectorstore(new_chunks)

        return JSONResponse(content={"message": "✅ PDF uploaded and indexed successfully."}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
