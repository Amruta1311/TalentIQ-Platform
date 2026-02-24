# tabs/gpu_test.py
import streamlit as st
import time
from resume_match.main import model, device

def show():
    st.header("GPU Test & Performance")
    st.write(f"Using device: {device.upper()}")

    # Benchmark inference time
    dummy_texts = ["Test"] * 10
    start = time.time()
    dummy_embs = [model.encode(t) for t in dummy_texts]
    end = time.time()

    st.metric("Inference Time for 10 encodings (seconds)", round(end - start, 3))
    st.write("Check if GPU is being used for acceleration above.")