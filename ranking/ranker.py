# tabs/ranking.py
import streamlit as st
from resume_match.main import model  # reuse loaded model
import pandas as pd
import numpy as np

# Placeholder functions
def rank_candidates(job_emb, resume_embs, candidates):
    scores = [np.dot(job_emb, r) / (np.linalg.norm(job_emb) * np.linalg.norm(r)) for r in resume_embs]
    ranked = sorted(zip(candidates, scores), key=lambda x: -x[1])
    return [{"candidate": c, "score": s} for c, s in ranked]

def get_all_jobs():
    return pd.DataFrame({
        "id": [1,2],
        "title": ["Data Scientist", "Quant Analyst"],
        "description": ["Job desc A", "Job desc B"]
    })

def get_all_resumes():
    return pd.DataFrame({
        "id": [1,2],
        "candidate": ["Alice", "Bob"],
        "resume": ["Resume text A", "Resume text B"]
    })

def show():
    st.header("Resume Ranking for a Job")
    jobs_df = get_all_jobs()
    candidates_df = get_all_resumes()
    selected_job = st.selectbox("Select Job", jobs_df['title'])

    if st.button("Rank Candidates"):
        job_text = jobs_df[jobs_df['title'] == selected_job]['description'].values[0]
        job_emb = model.encode(job_text)
        resume_texts = candidates_df['resume'].tolist()
        resume_embs = [model.encode(r) for r in resume_texts]
        candidates = candidates_df['candidate'].tolist()
        ranked = rank_candidates(job_emb, resume_embs, candidates)

        st.subheader("Top Candidates")
        st.dataframe(ranked)

        # Bar chart
        df_chart = pd.DataFrame(ranked)
        st.bar_chart(df_chart.set_index('candidate')['score'])