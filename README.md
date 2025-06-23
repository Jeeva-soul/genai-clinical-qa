---
title: GenAI Clinical Q&A Assistant
emoji: 🧠
colorFrom: indigo
colorTo: green
sdk: docker
app_file: Dockerfile
pinned: false
---
# 🧠 GenAI Clinical Q&A Assistant

A GenAI-powered clinical question-answering system that allows users to ask questions about medical PDFs, patient cases, or discharge notes — and get accurate, natural language answers.

---

## 🚀 Features

- 🔍 Semantic search over clinical documents using **FAISS** & **Sentence Transformers**
- 💬 Question answering via **FLAN-T5** (HuggingFace Inference API)
- 📄 Upload your own medical PDFs for live querying
- 🌐 Frontend built with **Streamlit** (no React/Node required)
- 🧠 Custom-trained on real medical CSVs converted into PDF
- ⚙️ Modular architecture using **FastAPI**, **Python**, and **Hugging Face**

---

## 📁 Project Structure

```
genai-clinical-qa/
├── backend/
│   ├── app.py                # FastAPI app for backend
│   ├── qa_engine.py          # Embedding + QA logic
│   ├── document_loader.py    # PDF text extraction
│   ├── embedding_store.py    # FAISS vector index
├── frontend/
│   └── app.py                # Streamlit UI
├── data/
│   └── clinical_docs/        # Sample/generated PDFs
├── generate_pdfs_from_csv.py # Create PDFs from medical CSVs
├── requirements.txt
└── .env                      # HuggingFace token (excluded from Git)
```

---

## 🛠 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/Jeeva-soul/genai-clinical-qa.git
cd genai-clinical-qa

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # (Windows)
# or
source venv/bin/activate     # (macOS/Linux)

# 3. Install required packages
pip install -r requirements.txt

# 4. Add HuggingFace token to .env
echo HUGGINGFACEHUB_API_TOKEN=your_token_here > .env

# 5. Run the backend
uvicorn backend.app:app --reload

# 6. In a new terminal, run the Streamlit frontend
cd frontend
streamlit run app.py
```

---

## 📬 Example API Request (Backend)

```
POST /ask
{
  "question": "What medications were prescribed?"
}
```

---

## 💻 Streamlit UI Features

- Elegant design with custom CSS
- Real-time question box with loading spinner
- Upload your own PDFs to instantly augment the knowledge base
- Beautifully styled answer container

---

## 📊 Dataset Used

- 🧠 [Brain Tumor Dataset (Kaggle)](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)
- 📄 Converted to PDFs to simulate real-world clinical documents

---

## 🧩 Future Enhancements

- 🧬 Clinical entity tagging (ICD-10, SNOMED)
- ☁️ Cloud deployment (Azure, Hugging Face Spaces)
- 🔁 Multiple LLM support (switch between APIs/local models)
- 📈 Session history & PDF content preview

---

## ⚠️ Security Note

Do **not** commit your `.env` or HuggingFace API keys to GitHub.
They are automatically excluded using `.gitignore`.

---

## 👨‍💻 Author

**Jeeva Manavalan**  
🎓 University of Texas at Arlington | Data Scientist | GenAI Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/jeeva-manavalan/) • [GitHub](https://github.com/Jeeva-soul)

---

## 📄 License

MIT License
