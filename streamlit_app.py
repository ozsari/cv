import streamlit as st
import requests
from PIL import Image
from io import BytesIO

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        img = Image.open(BytesIO(response.content))
        return img
    except Exception as e:
        st.error(f"Error loading image from {url}: {str(e)}")
        return None

st.set_page_config(page_title="Ahmet Ozsari - CV") # , layout="wide"

# Header
st.title("Ahmet Ozsari")
st.write("Experienced Data Engineer")
st.write("📍 4. Levent, Istanbul")
st.write("📧 ozsariahmet@yahoo.com | 🔗 [LinkedIn](https://linkedin.com/in/ahmet-ozsari-6615b756)")

# Summary
st.header("Summary")
st.write("""
Experienced Data Engineer with a strong background in business intelligence, data modeling, and cloud
services. Proficient in designing and implementing end-to-end data solutions, with a focus on AWS and
Google Cloud platforms. Adept at automating ETL processes and developing real-time monitoring
systems. Committed to continuous improvement and collaborative teamwork.
""")

# Skills
st.header("Skills")
skills = [
    "Data Integration and Processing",
    "Data Modeling and Warehouse Management",
    "Cloud Platforms (AWS, Google Cloud)",
    "Programming (Python, SQL)",
    "Data Pipelines and Workflows",
    "Team Collaboration",
    "Dashboards (Qlik, Power BI, Looker)"
]
col1, col2 = st.columns(2)
for i, skill in enumerate(skills):
    if i % 2 == 0:
        col1.write(f"• {skill}")
    else:
        col2.write(f"• {skill}")

# Work Experience
st.header("Work Experience")

def job(title, company, period, responsibilities):
    st.subheader(f"{title} - {company}")
    st.write(f"*{period}*")
    for r in responsibilities:
        st.write(f"• {r}")

job("Data Engineer", "Justlife", "May 2022 - Present", [
    "Redesigned the entire ELT infrastructure on Google Cloud, enhancing data processing efficiency.",
    "Automated data collection and transformation processes using Kubernetes, Airflow, and dbt.",
    "Streamlined processes with GitHub and GitSync for collaborative code contributions.",
    "Developed algorithms for alert mechanisms, achieving near real-time monitoring."
])

job("Data Engineer", "Modanisa", "Feb 2022 - May 2022", [
    "Assisted teams in implementing data lake solutions on AWS using Python.",
    "Led automation of workloads and ETL projects, improving data processing efficiency.",
    "Utilized Airflow, Presto/Trino, Docker, Kubernetes, and AWS services.",
    "Applied BigQuery and Google Analytics for optimized data analysis and reporting."
])

job("Business Intelligence Assistant Manager", "Modanisa", "Jul 2019 - Feb 2022", [
    "Transformed the team into federated development units for faster BI deployment.",
    "Migrated QlikView dashboards to Qlik Sense while gathering business requirements."
])

# Education
st.header("Education")
st.subheader("Bachelor of Computer Engineering")
st.write("Beykent University, Istanbul")
st.write("*Sep 2008 - June 2013*")

# Certifications
st.header("Certifications")
cert_col1, cert_col2, cert_col3 = st.columns(3)

with cert_col1:
    qlikview_logo = load_image("https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png")
    if qlikview_logo:
        st.image(qlikview_logo, width=100)
    st.write("QlikView Developer")

with cert_col2:
    qlik_sense_logo = load_image("https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png")
    if qlik_sense_logo:
        st.image(qlik_sense_logo, width=100)
    st.write("Administer and Maintain Qlik Sense")

with cert_col3:
    dbt_logo = load_image("https://github.com/user-attachments/assets/8d6a29cb-9fe2-451c-8684-2fdc13a96a42")
    if dbt_logo:
        st.image(dbt_logo, width=100)
    st.write("DBT Fundamentals")

# Additional Information
st.header("Additional Information")
st.write("**Languages:** English, Turkish")
st.write("**Technical Skills:** Data Engineering and Integration, Comprehensive ETL and ELT Processes, Data Modeling and Solution Development, Automation and Workflow Orchestration, Cloud Infrastructure Management, Business Intelligence and Advanced Analytics, Data Visualization, Data-Driven Decision Making")
