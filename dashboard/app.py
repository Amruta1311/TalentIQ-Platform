# app.py
import streamlit as st
import numpy as np
import torch
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="TalentIQ Dashboard")

st.title("TalentIQ Dashboard")

# Load model (runs once)
@st.cache_resource
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = SentenceTransformer("all-MiniLM-L6-v2", device=device)
    return model, device

model, device = load_model()

# Cosine similarity function
def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Input fields
resume = st.text_area("Paste Resume")
job = st.text_area("Paste Job Description")

if st.button("Match"):
    if not resume.strip() or not job.strip():
        st.warning("Please enter both Resume and Job Description!")
    else:
        # Encode and compute similarity
        r_emb = model.encode(resume)
        j_emb = model.encode(job)
        score = cosine(r_emb, j_emb)

        st.metric("Match Score", f"{round(float(score) * 100, 2)}%")
        st.write("Device used:", device.upper())