import streamlit as st
import requests

API_URL = "http://3.27.222.183/:8000/predict" 

st.title("Loan Approval Predictor")
st.markdown("Enter your details below:")

# Input fields
Applicant_Income = st.number_input("Income", min_value=1, value=300000)
Coapplicant_Income = st.number_input("coapplicant income", value=65000)
Employment_Status = st.selectbox("Are you Employed?", options=['Salaried', 'Self-employed', 'Contract', 'Unemployed'])
Marital_Status = st.selectbox("Are you Married", options=['Married', 'Single'])
Age = st.number_input("Age", value=35)
Dependents = st.number_input("No of Dependent", value=2)
Credit_Score =st.number_input("your credit score", value=789)
Existing_Loans = st.number_input("no. of existing loans", value=2)
DTI_Ratio= st.number_input("DTI ratio", min_value=0.0, max_value=0.99, value=0.7)
Savings= st.number_input("Savings", min_value=1, value=300000)
Collateral_Value= st.number_input("collateral value", value=200000)
Loan_Amount=  st.number_input("Loan amount", value=3000000)
Loan_Term= st.number_input("loan duration", value=36)
Loan_Purpose= st.selectbox("purpose of loan", options=['Personal', 'Car', 'Business', 'Home', 'Education'])
Property_Area= st.selectbox("property type", options=['Urban', 'Semiurban', 'Rural'])
Education_Level= st.selectbox("graduated or not", options=['Not Graduate', 'Graduate'])
Gender= st.selectbox("Gender", options=['Male', 'Female'])
Employer_Category=  st.selectbox("Employer Category", options=['Private', 'Government', 'Unemployed', 'MNC', 'Business'])


if st.button("Predict Approval"):
    input_data = {
        "Applicant_Income": Applicant_Income,
        "Coapplicant_Income": Coapplicant_Income,
        "Employment_Status": Employment_Status,
        "Marital_Status": Marital_Status,
        "Age": Age,
        "Dependents": Dependents,
        "Credit_Score": Credit_Score,
        "Existing_Loans": Existing_Loans,
        "DTI_Ratio": DTI_Ratio,
        "Savings": Savings,
        "Collateral_Value": Collateral_Value,
        "Loan_Amount": Loan_Amount,
        "Loan_Term": Loan_Term,
        "Loan_Purpose": Loan_Purpose,
        "Property_Area": Property_Area,
        "Education_Level": Education_Level,
        "Gender": Gender,
        "Employer_Category": Employer_Category
    }

    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Approval: **{result['predicted_category'][0]}**")
        else:
            st.error(f"API Error: {response.status_code}")
            st.write(response.json())

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to FastAPI server.")