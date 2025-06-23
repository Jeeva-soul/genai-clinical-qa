import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer

# Load sentence embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FLAN-T5 model for answer generation
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
t5_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

def get_top_k_context(index, vectors, chunks, query, k=3):
    query_vector = embedding_model.encode([query])
    D, I = index.search(np.array(query_vector).astype("float32"), k)
    return [chunks[i] for i in I[0]]

def ask_question(query, index, vectors, chunks):
    try:
        top_chunks = get_top_k_context(index, vectors, chunks, query)
        context = "\n".join(top_chunks)
        prompt = f"Answer the question based on the context below:\n\n{context}\n\nQuestion: {query}\nAnswer:"
        
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        outputs = t5_model.generate(**inputs, max_new_tokens=200)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return answer
    except Exception as e:
        return f"Error: {str(e)}"

