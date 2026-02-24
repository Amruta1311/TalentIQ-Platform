import streamlit as st
import requests

st.title("TalentIQ Dashboard")

resume = st.text_area("Paste Resume")
job = st.text_area("Paste Job Description")

if st.button("Match"):

    payload = {
        "resume": resume,
        "job": job
    }

    res = requests.post(
        "http://localhost:8000/match",
        json=payload
    )

    data = res.json()

    st.metric("Match Score", data["match_score"])
    st.write("Device:", data["device"])