# tabs/risk.py
import streamlit as st

# Placeholder bias computation
def compute_bias(ranked_resumes):
    return {"gender": 0.05, "age": 0.02, "data": ranked_resumes}

def show():
    st.header("Risk / Bias Monitoring")
    ranked_resumes = [{"candidate": "Alice", "score": 0.87}, {"candidate": "Bob", "score": 0.75}]
    bias_report = compute_bias(ranked_resumes)

    st.metric("Gender Bias Score", bias_report['gender'])
    st.metric("Age Bias Score", bias_report['age'])
    st.subheader("Detailed Data")
    st.dataframe(bias_report['data'])