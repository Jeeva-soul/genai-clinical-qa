from PyPDF2 import PdfReader
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(directory_path):
    docs = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            reader = PdfReader(os.path.join(directory_path, filename))
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
            docs.append(text)
    return docs

def split_into_chunks(documents, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "]
    )
    all_chunks = []
    for doc in documents:
        all_chunks.extend(splitter.split_text(doc))
    return all_chunks
