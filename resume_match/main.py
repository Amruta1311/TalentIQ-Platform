# tabs/resume_match.py
import streamlit as st
import torch
from sentence_transformers import SentenceTransformer
import numpy as np

# Load model (cached)
@st.cache_resource
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = SentenceTransformer("all-MiniLM-L6-v2", device=device)
    return model, device

model, device = load_model()

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def show():
    st.header("Resume-Job Matching")
    resume_text = st.text_area("Paste Resume", height=150)
    job_text = st.text_area("Paste Job Description", height=150)

    if st.button("Compute Match Score"):
        if not resume_text.strip() or not job_text.strip():
            st.warning("Please enter both Resume and Job Description!")
        else:
            r_emb = model.encode(resume_text)
            j_emb = model.encode(job_text)
            score = cosine(r_emb, j_emb)
            st.metric("Match Score", f"{round(float(score) * 100, 2)}%")
            st.write("Device used:", device.upper())