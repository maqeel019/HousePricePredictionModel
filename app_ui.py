
import streamlit as st
import numpy as np
import joblib

# Load the saved scaler and model
scaler = joblib.load('scaler.pkl')
model = joblib.load('house_price_model.pkl')

# Streamlit app title
st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="wide")
st.title("🏠 House Price Prediction App")
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)
# User inputs for the features
area = st.number_input("Enter Area (in sqft):", min_value=500, max_value=10000, step=100, value=5000)
bedrooms = st.number_input("Enter Number of Bedrooms:", min_value=0, max_value=10, step=1, value=0)
bathrooms = st.number_input("Enter Number of Bathrooms:", min_value=0, max_value=10, step=1, value=0)
stories = st.number_input("Enter Number of Stories:", min_value=0, max_value=5, step=1, value=2)
mainroad = st.selectbox("Is it on the Main Road?", ["Yes", "No"])
guestroom = st.selectbox("Is there a Guestroom?", ["Yes", "No"])
basement = st.selectbox("Does it have a Basement?", ["Yes", "No"])
hotwaterheating = st.selectbox("Does it have Hot Water Heating?", ["Yes", "No"])
airconditioning = st.selectbox("Does it have Air Conditioning?", ["Yes", "No"])
parking = st.number_input("Enter Number of Parking Spaces:", min_value=0, max_value=5, step=1, value=0)
prefarea = st.selectbox("Is it in a Preferred Area?", ["Yes", "No"])
furnishingstatus = st.selectbox("Furnishing Status:", ["Unfurnished", "Semi-Furnished", "Furnished"])

# Convert inputs into numeric values
mainroad = 1 if mainroad == "Yes" else 0
guestroom = 1 if guestroom == "Yes" else 0
basement = 1 if basement == "Yes" else 0
hotwaterheating = 1 if hotwaterheating == "Yes" else 0
airconditioning = 1 if airconditioning == "Yes" else 0
prefarea = 1 if prefarea == "Yes" else 0
furnishingstatus = {"Unfurnished": 0, "Semi-Furnished": 1, "Furnished": 2}[furnishingstatus]

# Prepare the input array
features = np.array([[
    area, bedrooms, bathrooms, stories, mainroad, guestroom,
    basement, hotwaterheating, airconditioning, parking,
    prefarea, furnishingstatus
]])

# Prediction button
if st.button("Predict Price"):
    # Apply scaling
    features_scaled = scaler.transform(features)
    
    # Make prediction
    predicted_price = model.predict(features_scaled)[0]
    
    # Display the result
    st.success(f"The predicted house price is: ${predicted_price:,.2f}")
