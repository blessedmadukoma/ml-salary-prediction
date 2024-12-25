import joblib
import pandas as pd
import streamlit as st

from helper import header_manipulation

st.set_page_config(page_title="Salary Prediction App")

# Streamlit configuration

st.title("Salary Prediction App")

st.write("To predict the salary, fill the details below:")

# import the dataset
salary_dataset = pd.read_csv("data/salary_data.csv")

# put column headers into lowercase and replace spaces with underscores
salary_dataset.columns = header_manipulation(salary_dataset)

# load the prediction model
pipeline = joblib.load("salary_prediction_pipeline.pkl")


# header
st.header("Job Information")

# user inputs
job_title = st.selectbox(
    "Job Title",
    salary_dataset['job_title'].unique())

job_simp = st.selectbox(
    "Job Title (Simplified)",
    salary_dataset['job_simp'].unique())

job_state = st.selectbox(
    "State",
    salary_dataset['job_state'].unique()
)

seniority = st.selectbox(
    "Seniority Level",
    salary_dataset["seniority"].unique()
)

sector = st.selectbox(
    "Sector",
    salary_dataset["sector"].unique()
)

type_of_ownership = st.selectbox(
    "Company Ownership",
    salary_dataset['type_of_ownership'].unique()
)

size = st.selectbox(
    "Company Size",
    salary_dataset["size"].unique()
)

industry = st.selectbox(
    "Industry",
    salary_dataset["industry"].unique()
)

location = st.selectbox(
    "Location",
    salary_dataset["location"].unique()
)

employer_provided_bool = st.selectbox(
    "Employer Provided",
    ["True" if x == 1 else "False"
        for x in salary_dataset["employer_provided"].unique()]
)

employer_provided = 1 if employer_provided_bool else 0

# Boolean inputs
st.header("Skills")

aws = st.checkbox("AWS")
excel = st.checkbox("Excel")
python_yn = st.checkbox("Python")
r_yn = st.checkbox("R")
spark = st.checkbox("Spark")
hourly = st.checkbox("Hourly Job")

if st.button("Predict Salary"):
    input_data = pd.DataFrame({
        'job_title': [job_title],
        'job_simp': [job_simp],
        'job_state': [job_state],
        'seniority': [seniority],
        'sector': [sector],
        'industry': [industry],
        'employer_provided': [employer_provided],
        'location': [location],
        'type_of_ownership': [type_of_ownership],
        'size': [size],
        'aws': [int(aws)],
        'excel': [int(excel)],
        'python_yn': [int(python_yn)],
        'r_yn': [int(r_yn)],
        'spark': [int(spark)],
        'hourly': [int(hourly)],
    })

    # Predict salary
    try:
        salary_prediction = pipeline.predict(input_data)
        st.success(f"Predicted Salary: ${salary_prediction[0]:,.2f}")
        st.balloons()
    except Exception as e:
        st.error(f"Error predicting job salary: {e}")
