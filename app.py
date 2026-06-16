#tells Jupyter to Save the code in this cell into a file named app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import joblib

# Load dataset
df = pd.read_csv("real_estate.csv")
df['view'] = df['view'].apply(lambda x: 1 if x == "Sea view" else 0)

#creating a new variable and dropping 'year'
current_year = 2026
df['property_age'] = current_year - df['year']
df = df.drop('year', axis=1)

X = df.drop(['price'], axis=1) 
y = df['price'] 

#Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train model
model = LinearRegression()
model.fit(X_train, y_train)

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
    prediction = model.predict(np.array([[Size,Property_age, View]]))[0]
    st.success(f"Estimated Price: UGX {prediction:,.2f}")
