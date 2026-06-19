#tells Jupyter to Save the code in this cell into a file named app.py
import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("price_model.pkl")
st.title("HOUSE PRICE Prediction App")
st.markdown("""
<div style="
    background-color:white;
    padding:20px;
    border-radius:15px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
">
<h3>Property Details</h3>
</div>
""", unsafe_allow_html=True)

# User inputs
Size = st.number_input("Size (sq ft)", min_value=500, max_value=5000, step=50)
Property_age = st.number_input("property_age")
View = st.selectbox("Sea View?", ["No", "Yes"])
View = 1 if View == "Yes" else 0

# Predict button
if st.button("Predict Price"):
     features = np.array([[Size, Property_age, View]])
     prediction = model.predict(features)[0]
     st.success(f"Estimated Price: UGX {prediction:,.2f}")
     st.metric(label="Predicted Price",value=f"UGX {prediction:,.0f}")
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

st.image(
    "https://images.unsplash.com/photo-1560518883-ce09059eeffa",
    use_container_width=True
)
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/69/69524.png",
    width=100
)
