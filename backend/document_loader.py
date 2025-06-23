from PyPDF2 import PdfReader
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load all PDF documents from a folder
def load_documents(directory_path):
    docs = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            reader = PdfReader(os.path.join(directory_path, filename))
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
            docs.append(text)
    return docs

# Split documents into manageable chunks
def split_into_chunks(documents, chunk_size=500, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = []
    for doc in documents:
        chunks.extend(text_splitter.split_text(doc))
    return chunks

# Parse a single PDF (uploaded) and split into chunks
def parse_pdf_to_chunks(pdf_path):
    reader = PdfReader(pdf_path)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return split_into_chunks([text])
