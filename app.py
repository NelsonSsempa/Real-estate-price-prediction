#tells Jupyter to Save the code in this cell into a file named app.py
import streamlit as st
import joblib

# Load trained model
model = joblib.load("price_model.pkl")
st.title("PRICE Prediction App")
st.write("Enter real estate information below:")

# User inputs
Size = st.number_input("Size (sq ft)", min_value=500, max_value=5000, step=50)
Property_age = st.number_input("property_age")
View = st.selectbox("Sea View?", ["No", "Yes"])
View = 1 if View == "Yes" else 0

# Predict button
if st.button("Predict Price"):
     features = np.array([[size, property_age, view]])
     prediction = model.predict(features)[0]
     st.success(f"Estimated Price: UGX {prediction:,.2f}")
     st.metric(label="Predicted Price",value=f"UGX {prediction:,.0f}")


