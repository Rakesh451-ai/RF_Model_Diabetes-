import streamlit as st
import joblib

model = joblib.load("Diabetes_Status.pkl")

st.title("Diabetes Prediction")
# Features
insulin = st.number_input("Insulin_Levels", min_value=0.0)
ogtt = st.number_input("OGTT", min_value=0.0)
creatinine = st.number_input("Creatinine_Levels", min_value=0.0)
random_glucose = st.number_input("Random_Blood_Glucose", min_value=0.0)
ldl = st.number_input("LDL_Cholesterol", min_value=0.0)
uric_acid = st.number_input("Uric_Acid_Levels", min_value=0.0)
alt = st.number_input("ALT", min_value=0.0)
ast = st.number_input("AST", min_value=0.0)
fasting_glucose = st.number_input("Fasting_Blood_Glucose", min_value=0.0)
hba1c = st.number_input("HbA1c", min_value=0.0)

if st.button("Predict"):
    data = [[
        insulin,
        ogtt,
        creatinine,
        random_glucose,
        ldl,
        uric_acid,
        alt,
        ast,
        fasting_glucose,
        hba1c
    ]]

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Diabetes detected")
    else:
        st.success("No diabetes detected")
