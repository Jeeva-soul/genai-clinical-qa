#!/bin/bash

# Start FastAPI backend
uvicorn backend.app:app --host 0.0.0.0 --port 8000 &

# Start Streamlit frontend
streamlit run app.py --server.port 7860 --server.address 0.0.0.0
