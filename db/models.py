# tabs/database.py
import streamlit as st
import pandas as pd

# db/models.py
import pandas as pd

# Dummy Resume Database
def get_all_resumes():
    """
    Returns a DataFrame of sample resumes.
    """
    data = [
        {
            "id": 1,
            "candidate": "Alice Johnson",
            "resume": """Alice Johnson
                            Education: B.Sc. Computer Science, University of XYZ
                            Skills: Python, SQL, Pandas, Machine Learning, NLP
                            Experience:
                            - Data Analyst at TechCorp (2021-2023): Analyzed sales and customer data, built dashboards using Python & SQL.
                            - ML Intern at InnovateAI (2020-2021): Built predictive models for customer churn.
                            Certifications: AWS Certified Data Analytics, Google Data Analytics"""
        },
        {
            "id": 2,
            "candidate": "Bob Smith",
            "resume": """Bob Smith
                            Education: M.Sc. Statistics, University of ABC
                            Skills: R, Python, SQL, Time Series Analysis, Financial Modeling
                            Experience:
                            - Quantitative Analyst Intern at FinancePro (2022-2023): Developed risk models and backtested trading strategies.
                            - Data Scientist at DataSolutions (2020-2022): Built predictive models for retail sales and inventory optimization.
                            Certifications: CFA Level 1, SAS Certified Data Scientist"""
        }
    ]
    return pd.DataFrame(data)

# Dummy Job Database
def get_all_jobs():
    """
    Returns a DataFrame of sample job postings.
    """
    data = [
        {
            "id": 1,
            "title": "Data Scientist",
            "description": """We are looking for a Data Scientist with experience in Python, Machine Learning, and NLP. 
                Responsibilities include building predictive models, analyzing datasets, and collaborating with cross-functional teams."""
        },
        {
            "id": 2,
            "title": "Quantitative Analyst",
            "description": """Seeking a Quantitative Analyst with strong skills in Python, R, and Financial Modeling. 
                    Tasks include developing risk models, analyzing time series data, and supporting trading strategies."""
        }
    ]
    return pd.DataFrame(data)

def get_match_scores():
    return pd.DataFrame({
        "candidate": ["Alice", "Bob"],
        "job": ["Data Scientist", "Quant Analyst"],
        "score": [0.87, 0.75]
    })

def show():
    st.header("Database Overview")
    resumes = get_all_resumes()
    jobs = get_all_jobs()
    matches = get_match_scores()

    st.subheader("Resumes")
    st.dataframe(resumes)

    st.subheader("Jobs")
    st.dataframe(jobs)

    st.subheader("Match Scores")
    st.dataframe(matches)