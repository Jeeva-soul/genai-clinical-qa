import streamlit as st
import requests
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="GenAI Clinical Q&A Assistant", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
        .main { background-color: #f8f9fa; }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 16px;
        }
        .stTextInput>div>div>input {
            border-radius: 8px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.image("https://img.icons8.com/ios/452/brain.png", width=80)
st.markdown("""
    # 🧠 GenAI Clinical Q&A Assistant  
    <small>AI-powered medical document analysis and question answering</small>
""", unsafe_allow_html=True)

st.write("Upload clinical documents or ask natural language questions. The assistant will infer answers using its trained knowledge base.")

# --- Sidebar ---
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/medical-doctor.png", width=80)
    st.markdown("## ℹ️ Instructions")
    st.write("""
    - Upload a clinical PDF to refresh knowledge base.
    - Ask a clinical question below.
    - Get real-time answers from the model.
    """)
    st.markdown("---")
    st.caption("Built with ❤️ using FastAPI, HuggingFace, and Streamlit")

    uploaded_file = st.file_uploader("📄 Upload a clinical PDF", type=["pdf"])
    if uploaded_file:
        st.info("File selected. Ready to send.")
        if st.button("📤 Upload & Index"):
            with st.spinner("Uploading and refreshing vectorstore..."):
                files = {"pdf": uploaded_file.getvalue()}
                try:
                    response = requests.post("http://127.0.0.1:8000/upload_pdf", files={"file": uploaded_file})
                    if response.status_code == 200:
                        st.success("✅ File uploaded and indexed successfully!")
                    else:
                        st.error(f"❌ Backend error: HTTP {response.status_code}")
                except Exception as e:
                    st.error(f"⚠️ Upload failed: {e}")

# --- Input Form ---
with st.form("ask_form"):
    question = st.text_input("💬 Enter your clinical question:")
    submit_btn = st.form_submit_button("🚀 Get Answer")

if submit_btn:
    if question.strip():
        with st.spinner("Analyzing question and retrieving relevant answers..."):
            try:
                res = requests.post("http://127.0.0.1:8000/ask", json={"question": question})
                if res.status_code == 200:
                    answer = res.json().get("answer", "⚠️ No answer returned.")
                    st.success("✅ Answer:")
                    st.markdown(f"""
                    <div style="background-color:#fdfdfd;padding:15px;border-radius:10px;
                                color:#111;font-size:16px;line-height:1.6;">
                        {answer}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(f"❌ Backend error: HTTP {res.status_code}")
            except Exception as e:
                st.error(f"⚠️ Request failed: {e}")
    else:
        st.warning("❗ Please enter a valid question.")
