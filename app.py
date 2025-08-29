import streamlit as st
import pandas as pd
import joblib

#load cleaned dataset
df = pd.read_csv("cleaned_Recall.csv")

# Load the trained model
model = joblib.load("recall_model.pkl")

st.set_page_config(page_title="Recall Prediction App", layout="wide")
st.title("Recall Prediction App")

st.write("Enter the details below to predict recall classification:")

# Input form
with st.form("recall_form"):
    Manufacturer = st.selectbox("Select Manufacturer", options = df['Manufacturer'].unique())
    Component = st.selectbox("Select Component", options = df['Component'].unique())
    Recall_Type = st.selectbox("Select Recall Type", options = df['Recall Type'].unique())
    Recall_Year = st.selectbox("Select Year", options = df['Recall Year'].unique())
    Recall_Month = st.selectbox("Select Month", list(range(1, 13)))
    Recall_Description = st.selectbox("Select Recall Description",options = df['Recall Description'].unique())

    submit = st.form_submit_button("Predict")

if submit:
    # Create dataframe with new input
    new_data = pd.DataFrame([{
        "Manufacturer" : Manufacturer,
        "Component" : Component,
        "Recall Type" : Recall_Type,
        "Recall Year": Recall_Year,
        "Recall Month":Recall_Month,
        "Recall Description": Recall_Description
    }])

     # Prediction
    prediction = model.predict(new_data)[0]
    prediction_proba = model.predict_proba(new_data)[0]  # probabilities

    mapping = {0: "Low Impact", 1: "Medium Impact", 2: "High Impact"}
    st.success(f"Prediction: {mapping.get(prediction, prediction)}")

    # Show probabilities for transparency
    st.subheader("Prediction Probabilities")
    for i, prob in enumerate(prediction_proba):
        st.write(f"{mapping[i]}: {prob:.2%}")

    # Extra insight (example)
    if prediction == 2:
        st.warning("⚠️ High Impact Recall — urgent attention needed!")
    elif prediction == 1:
        st.info("Moderate Impact — requires follow-up.")
    else:
        st.success("Low Impact — minimal risk detected.")
