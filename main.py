import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page configuration
st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊", layout="wide")

# Load the saved model
@st.cache_resource
def load_model():
    # Replace 'churn_model_grid.pkl' with your actual saved model filename
    return joblib.load('churn_model_grid.pkl')

model = load_model()

st.title("Customer Churn Prediction App")
st.write("Enter the customer details below to predict whether they are likely to churn.")

# Create input layout using columns
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Demographics & Account")
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)

with col2:
    st.subheader("Services Subscribed")
    phone_service = st.selectbox("Phone Service", ["No", "Yes"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes"])
    online_security = st.selectbox("Online Security", ["No", "Yes"])
    online_backup = st.selectbox("Online Backup", ["No", "Yes"])
    device_protection = st.selectbox("Device Protection", ["No", "Yes"])
    tech_support = st.selectbox("Tech Support", ["No", "Yes"])

with col3:
    st.subheader("Billing & Contracts")
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes"])
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes"])
    paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
    monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=50.0)
    total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=500.0)

# Categorical choices for one-hot encoded fields
st.subheader("Plan & Payment Details")
c1, c2 = st.columns(2)
with c1:
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
with c2:
    payment_method = st.selectbox("Payment Method", [
        "Electronic check", 
        "Mailed check", 
        "Bank transfer (automatic)", 
        "Credit card (automatic)"
    ])

# Convert inputs into the exact column schema required by the model
input_data = {
    'gender': 0 if gender == "Male" else 1,
    'SeniorCitizen': senior_citizen,
    'Partner': 1 if partner == "Yes" else 0,
    'Dependents': 1 if dependents == "Yes" else 0,
    'tenure': tenure,
    'PhoneService': 1 if phone_service == "Yes" else 0,
    'MultipleLines': 1 if multiple_lines == "Yes" else 0,
    'OnlineSecurity': 1 if online_security == "Yes" else 0,
    'OnlineBackup': 1 if online_backup == "Yes" else 0,
    'DeviceProtection': 1 if device_protection == "Yes" else 0,
    'TechSupport': 1 if tech_support == "Yes" else 0,
    'StreamingTV': 1 if streaming_tv == "Yes" else 0,
    'StreamingMovies': 1 if streaming_movies == "Yes" else 0,
    'PaperlessBilling': 1 if paperless_billing == "Yes" else 0,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges,
    
    # One-hot encoded columns
    'InternetService_Fiber optic': True if internet_service == "Fiber optic" else False,
    'InternetService_No': True if internet_service == "No" else False,
    'Contract_One year': True if contract == "One year" else False,
    'Contract_Two year': True if contract == "Two year" else False,
    'PaymentMethod_Credit card (automatic)': True if payment_method == "Credit card (automatic)" else False,
    'PaymentMethod_Electronic check': True if payment_method == "Electronic check" else False,
    'PaymentMethod_Mailed check': True if payment_method == "Mailed check" else False,
}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

st.divider()

# Prediction button
if st.button("Predict Churn", type="primary", use_container_width=True):
    prediction = model.predict(input_df)[0]
    prediction_proba = model.predict_proba(input_df)[0]
    
    st.subheader("Prediction Results")
    if prediction == 1:
        st.error(f"⚠️ **The customer is likely to CHURN.** (Probability: {prediction_proba[1]:.2%})")
    else:
        st.success(f"✅ **The customer is likely to STAY (Not Churn).** (Probability of staying: {prediction_proba[0]:.2%})")