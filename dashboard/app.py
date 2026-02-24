# app.py
import sys
import os

sys.path.append(os.path.dirname(__file__))  # adds dashboard folder to path
import streamlit as st

from resume_match import main
from db import models
from ranking import ranker
from risk import bias_check
from benchmarks import gpu_test

st.set_page_config(page_title="TalentIQ Dashboard", layout="wide")
st.title("TalentIQ Dashboard")

# Create tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Resume-Job Match", "Database", "Ranking", "Risk/Bias", "GPU Test"
])

with tab1:
    main.show()

with tab2:
    models.show()

with tab3:
    ranker.show()

with tab4:
    bias_check.show()

with tab5:
    gpu_test.show()