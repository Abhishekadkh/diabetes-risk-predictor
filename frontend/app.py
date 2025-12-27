import streamlit as st
import numpy as np
import joblib

# Load your trained pipeline
pipeline = joblib.load("../artifacts/diabetes_pipeline.pkl")

# Page config
st.set_page_config(
    page_title="Diabetes Risk Predictor",
    page_icon="💉",
    layout="centered"
)

# Title and description
st.markdown(
    "<h1 style='text-align: center; color: #ff6a00;'>💉 Diabetes Risk Predictor</h1>", 
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: #fff; background-color: #66a6ff; padding: 10px; border-radius: 10px;'>"
    "Enter your health information below to check your risk of diabetes."
    "</p>", 
    unsafe_allow_html=True
)

st.markdown("---")

# Organize inputs in two columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=35)
    glucose = st.number_input("Glucose", min_value=0, max_value=200, value=120)
    bp = st.number_input("Blood Pressure", min_value=0, max_value=150, value=70)
    skin = st.number_input("Skin Thickness", min_value=0, max_value=100, value=30)

with col2:
    insulin = st.number_input("Insulin", min_value=0, max_value=900, value=100)
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=28.0, step=0.1)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5, step=0.01)
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)


st.markdown("---")

# Predict button
if st.button("Predict"):
    user_input = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = pipeline.predict(user_input)[0]
    prediction_prob = pipeline.predict_proba(user_input)[0][1]

    # Display prediction result
    if prediction == 1:
        st.error(f"⚠️ High risk of diabetes!")
    else:
        st.success(f"✅ Low risk of diabetes.")

    # Show probability
    st.markdown(
        f"<h3 style='text-align:center;'>Probability of Diabetes: <span style='color:#ff6a00;'>{prediction_prob*100:.2f}%</span></h3>",
        unsafe_allow_html=True
    )

    # Optional progress bar for visual appeal
    st.progress(prediction_prob)
