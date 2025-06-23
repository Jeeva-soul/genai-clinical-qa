# 🧠 GenAI Clinical Q&A Assistant

A GenAI-powered clinical question-answering system that allows users to ask questions about patient cases, discharge notes, or medical PDFs — and get accurate answers in natural language.

---

## 🚀 Features

- 🔍 Semantic search over clinical documents using **Sentence Transformers**
- 💬 Natural Language QA using **FLAN-T5** or **local Transformers**
- 📄 Upload & index your own PDFs (e.g., discharge notes, lab reports)
- 🧠 Custom-trained on real medical CSVs converted to PDF
- 🧰 Built with **Python**, **FastAPI**, **FAISS**, **Hugging Face Transformers**

---

## 📁 Project Structure

```
genai-clinical-qa/
├── backend/
│   ├── app.py                  # FastAPI app for inference
│   ├── qa_engine.py           # Embedding + QA logic
│   ├── document_loader.py     # PDF parsing logic
│   ├── embedding_store.py     # FAISS vectorstore setup
├── data/
│   └── clinical_docs/         # Sample PDFs or generated ones
├── generate_pdfs_from_csv.py  # Convert CSV rows to PDFs
├── requirements.txt
└── .env                       # HuggingFace API Key (excluded)
```

---

## 🛠 Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/Jeeva-soul/genai-clinical-qa.git
cd genai-clinical-qa

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add HuggingFace token in a .env file
HUGGINGFACEHUB_API_TOKEN=your_token_here

# 5. Run the FastAPI server
uvicorn backend.app:app --reload
```

---

## 📬 Example API Request

```
POST /ask
{
  "question": "What medications were prescribed?"
}
```

---

## 📊 Dataset Used

- 🧠 [Brain Tumor Dataset (Kaggle)](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)
- 📄 Converted to PDFs to simulate real clinical documents

---

## 🧩 Future Roadmap

- 🔁 Streamlit or React frontend interface
- 🏥 Clinical entity recognition (ICD-10 / SNOMED tagging)
- ☁️ Deployment on Hugging Face Spaces or Azure App Service
- 🧠 Option to switch between open-source LLMs and HuggingFace API

---

## 👨‍💻 Author

**Jeeva Manavalan**  
🎓 UTA | Data Scientist | AI Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/jeeva-manavalan/) • [GitHub](https://github.com/Jeeva-soul)

---

## 📄 License

MIT License
