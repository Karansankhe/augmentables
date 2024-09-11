import streamlit as st
import requests
import numpy as np

# Streamlit app
st.title('Loan Approval Prediction System')

# Collecting user input
gender = st.selectbox('Gender', ('Male', 'Female'))
married = st.selectbox('Married', ('Yes', 'No'))
dependents = st.selectbox('Dependents', ('0', '1', '2', '3+'))
education = st.selectbox('Education', ('Graduate', 'Not Graduate'))
self_employed = st.selectbox('Self Employed', ('Yes', 'No'))
applicant_income = st.number_input('Applicant Income', min_value=0)
coapplicant_income = st.number_input('Coapplicant Income', min_value=0)
loan_amount = st.number_input('Loan Amount (in thousands)', min_value=0)
loan_amount_term = st.number_input('Loan Amount Term (in months)', min_value=12)
credit_history = st.selectbox('Credit History', ('Good', 'Poor'))
property_area = st.selectbox('Property Area', ('Rural', 'Semiurban', 'Urban'))

# Encoding inputs
gender = 1 if gender == 'Male' else 0
married = 1 if married == 'Yes' else 0
dependents = 4 if dependents == '3+' else int(dependents)
education = 1 if education == 'Graduate' else 0
self_employed = 1 if self_employed == 'Yes' else 0
credit_history = 1 if credit_history == 'Good' else 0
property_area_mapping = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}
property_area = property_area_mapping[property_area]

# Creating input data
input_data = {
    'Gender': gender,
    'Married': married,
    'Dependents': dependents,
    'Education': education,
    'Self_Employed': self_employed,
    'ApplicantIncome': applicant_income,
    'CoapplicantIncome': coapplicant_income,
    'LoanAmount': loan_amount,
    'Loan_Amount_Term': loan_amount_term,
    'Credit_History': credit_history,
    'Property_Area': property_area
}

# Button to make prediction
if st.button('Predict Loan Status'):
    # Sending POST request to Flask API
    response = requests.post('http://127.0.0.1:5000/predict', json=input_data)
    
    # Checking the response
    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Loan Status: {prediction['Loan_Status']}")
    else:
        st.error("Error: Unable to get prediction. Please check your inputs or try again later.")
