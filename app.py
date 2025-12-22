import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="Credit Default Predict", page_icon="💳", layout="wide")

# --- CUSTOM CSS AND ANIMATIONS ---
st.markdown("""
    <style>
    /* Main Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* Title Animation */
    @keyframes fadeInDown {
        0% { opacity: 0; transform: translateY(-30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .main-title {
        animation: fadeInDown 1.2s ease-out;
        text-align: center;
        color: #1e3d59;
        font-family: 'Helvetica Neue', sans-serif;
        padding: 20px;
    }

    /* Pulsing Risk Box for High Risk */
    @keyframes pulse {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 0, 0, 0.4); }
        70% { transform: scale(1.02); box-shadow: 0 0 0 15px rgba(255, 0, 0, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 0, 0, 0); }
    }
    .high-risk-box {
        padding: 25px;
        border-radius: 15px;
        background-color: #ffe5e5;
        border: 2px solid #ff4b4b;
        color: #990000;
        text-align: center;
        animation: pulse 2s infinite;
    }

    /* Success Box for Low Risk */
    .low-risk-box {
        padding: 25px; 
        border-radius: 15px;
        background-color: #e5ffe5;
        border: 2px solid #28a745;
        color: #155724;
        text-align: center;
    }

    /* Input Card Styling */
    div[data-testid="stVerticalBlock"] > div:has(div.stNumberInput) {
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Load the model
try:
    with open('Dec_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file 'Dec_model.pkl' not found. Please ensure it is in the same directory.")

# Header
st.markdown('<h1 class="main-title">💳 Credit Card Defaulter Prediction</h1>', unsafe_allow_html=True)


main_col1, main_col2 = st.columns([1, 1], gap="large")

with main_col1:
    st.subheader("👤 Personal Profile")
    LIMIT_BALANCE = st.number_input("Limit Balance (NT$)", min_value=0, value=50000)
    EDUCATION = st.selectbox("Education Level", options=[1, 2, 3, 4, 5, 6], index=1, 
                            format_func=lambda x: {1:'University', 2 :'Graduate school', 3:'High School', 4:'Unknown',5: 'Others',6:'0'}[x])
    MARRIAGE = st.selectbox("Marital Status", options=[1, 2, 3, 4], index=1, 
                           format_func=lambda x: {1:'Married', 2:'Single', 3:'Others',4:'0'}[x])
    Age = st.number_input("Age", min_value=18, max_value=100, value=30)

    st.subheader("📊 Payment History (Monthly Delay)")
    c1, c2 = st.columns(2)
    with c1:
        PAY_0 = st.number_input("Sept Delay", min_value=-2, max_value=8, value=0)
        PAY_2 = st.number_input("Aug Delay", min_value=-2, max_value=8, value=0)
        PAY_3 = st.number_input("July Delay", min_value=-2, max_value=8, value=0)
    with c2:
        PAY_4 = st.number_input("June Delay", min_value=-2, max_value=8, value=0)
        PAY_5 = st.number_input("May Delay", min_value=-2, max_value=8, value=0)
        PAY_6 = st.number_input("April Delay", min_value=-2, max_value=8, value=0)

with main_col2:
    st.subheader("📑 Bill Amounts")
    b1, b2 = st.columns(2)
    with b1:
        BILL_AMT1 = st.number_input("Bill Sept", min_value=0, value=1000)
        BILL_AMT2 = st.number_input("Bill Aug", min_value=0, value=1000)
        BILL_AMT3 = st.number_input("Bill July", min_value=0, value=1000)
    with b2:
        BILL_AMT4 = st.number_input("Bill June", min_value=0, value=1000)
        BILL_AMT5 = st.number_input("Bill May", min_value=0, value=1000)
        BILL_AMT6 = st.number_input("Bill April", min_value=0, value=1000)

    st.subheader("💰 Repayment Amounts")
    p1, p2 = st.columns(2)
    with p1:
        PAY_AMT1 = st.number_input("Paid Sept", min_value=0, value=1000)
        PAY_AMT2 = st.number_input("Paid Aug", min_value=0, value=1000)
        PAY_AMT3 = st.number_input("Paid July", min_value=0, value=1000)
    with p2:
        PAY_AMT4 = st.number_input("Paid June", min_value=0, value=1000)
        PAY_AMT5 = st.number_input("Paid May", min_value=0, value=1000)
        PAY_AMT6 = st.number_input("Paid April", min_value=0, value=1000)

# Preparation of Data
input_data = pd.DataFrame({
    'LIMIT_BAL': [LIMIT_BALANCE], 
    'EDUCATION': [EDUCATION], 
    'MARRIAGE': [MARRIAGE], 
    'AGE': [Age],
    'PAY_0': [PAY_0], 
    'PAY_2': [PAY_2], 
    'PAY_3': [PAY_3], 
    'PAY_4': [PAY_4], 
    'PAY_5': [PAY_5], 
    'PAY_6': [PAY_6],
    'BILL_AMT1': [BILL_AMT1], 
    'BILL_AMT2': [BILL_AMT2], 
    'BILL_AMT3': [BILL_AMT3], 
    'BILL_AMT4': [BILL_AMT4], 
    'BILL_AMT5': [BILL_AMT5], 
    'BILL_AMT6': [BILL_AMT6],
    'PAY_AMT1': [PAY_AMT1], 
    'PAY_AMT2': [PAY_AMT2], 
    'PAY_AMT3': [PAY_AMT3], 
    'PAY_AMT4': [PAY_AMT4], 
    'PAY_AMT5': [PAY_AMT5], 
    'PAY_AMT6': [PAY_AMT6]
})

st.markdown("---")
# Centered Button
_, center_btn, _ = st.columns([1, 1, 1])
with center_btn:
    predict_clicked = st.button("🚀 Analyze Credit Risk", use_container_width=True)

if predict_clicked:
    # Prediction
    prob = model.predict_proba(input_data)[:, 1][0]
    
    # Logic for Risk Display
    if prob >= 0.5:
        risk_class = "high-risk-box"
        status = "CRITICAL: High Default Risk"
        desc = "The model predicts a high likelihood of payment failure. Caution is advised."
    else:
        risk_class = "low-risk-box"
        status = "STABLE: Low Default Risk"
        desc = "Customer behavior aligns with reliable repayment patterns."

    # Animated Result Output
    st.markdown(f"""
        <div class="{risk_class}">
            <h1 style="margin:0; font-size:30px;">{status}</h1>
            <h2 style="margin:0; opacity: 0.8; font-size: 22px;">Probability Score: {prob:.2%}</h2>
            <p style="font-size: 18px; margin-top: 10px;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.progress(float(prob))