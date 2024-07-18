import streamlit as st
from PIL import Image
import requests
from io import BytesIO

def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

st.set_page_config(page_title="Ahmet Ozsari - CV") # , layout="wide"


# Header
st.title("Ahmet Ozsari")
st.subheader("Data Engineer")
st.write("📍 Istanbul, TURKEY")
st.write("📧 ozsariahmet@yahoo.com | 🔗 [LinkedIn](https://linkedin.com/in/ahmet-ozsari-6615b756)")

# Summary
st.header(':blue[Summary]', divider='blue')
st.write("""
Experienced Data Engineer with a strong background in business intelligence, data modeling, and cloud
services. Proficient in designing and implementing end-to-end data solutions, with a focus on AWS and
Google Cloud platforms. Adept at automating ETL processes and developing real-time monitoring
systems. Committed to continuous improvement and collaborative teamwork.
""")

# Skills
st.header(':blue[Skills]', divider='blue')
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
st.header(':blue[Work Experience]', divider='blue')

def job(title, company, period, responsibilities):
    st.subheader(f"{title} - {company}")
    st.write(f"*{period}*")
    for r in responsibilities:
        st.write(f"• {r}")

job("Data Engineer", "Justlife", "May 2022 - Present", [
    "Redesigned the entire ELT infrastructure on Google Cloud, enhancing data processing efficiency.",
    "Automated data collection and transformation processes using Kubernetes, Airflow, and dbt.",
    "Streamlined processes with GitHub and GitSync for collaborative code contributions.",
    "Developed algorithms for alert mechanisms, achieving near real-time monitoring of operational issues and significantly increasing booking rates."
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

job("Senior Business Intelligence Specialist", "Zubizu", "Oct 2016 - Jul 2019", [
    "Developed dashboards that enabled senior executives to make data-driven strategic and operational decisions.",
    "Planned, designed, and implemented end-to-end BI solutions using SSIS and Power BI, enhancing data analysis capabilities.",
    "Created Qlik Widgets to improve visualization efficiency and user experience.",
    "Collaborated closely with internal teams and Dogus companies to understand and implement customized Qlik solutions using Agile delivery methods.",
    "Contributed to the implementation of a mobile app environment, significantly enhancing Qlik Sense usage."
])

job("BI Consultant", "Qlik Turkey", "Nov 2013 - Oct 2016", [
    "Successfully collaborated with a diverse range of clients, contributing to the development and implementation of BI processes and Qlik Dashboards.",
    "Delivered consulting services, providing expertise in BI infrastructure implementation and technical guidance to a diverse clientele, including advising on server acquisition, installation, security, governance, and automated reports.",
    "Conducted comprehensive hands-on training sessions for large user groups, ensuring proficient utilization of tools and processes."
])

# Certifications
st.header(':blue[Certifications]', divider='blue')

cert_col1, cert_col2 = st.columns(2)

with cert_col1:
    qlik_logo = load_image("https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png")
    st.image(qlik_logo, width=100)
    st.write("QlikView Developer")

with cert_col2:
    st.image(qlik_logo, width=100)
    st.write("Administer and Maintain Qlik Sense")

# Education
st.header(':blue[Education]', divider='blue')
st.subheader("Bachelor of Computer Engineering")
st.write("Beykent University, Istanbul")
st.write("*Sep 2008 - June 2013*")

# Additional Information
st.header(':blue[Additional Information]', divider='blue')
st.write("**Languages:** English, Turkish")
st.write("**Technical Skills:** Data Engineering and Integration, Comprehensive ETL and ELT Processes, Data Modeling and Solution Development, Automation and Workflow Orchestration, Cloud Infrastructure Management, Business Intelligence and Advanced Analytics, Data Visualization, Data-Driven Decision Making")
