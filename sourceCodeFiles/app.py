import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

st.set_page_config(page_title="Climate-Driven Disease Outbreak Prediction", layout="wide")  
st.title("Climate-Driven Disease Outbreak Prediction")
st.write("Predicting dengue disease outbreaks based on climate data using ML.")

# Sidebar for user inputs
st.sidebar.header("Input Parameters")

def get_user_input():
    avg_temp_c = st.sidebar.slider("Average Temperature (°C)", -10.0, 50.0, 25.0)
    precipitation_mm = st.sidebar.slider("Precipitation (mm)", 0.0, 500.0, 100.0)
    uv_index = st.sidebar.slider("UV Index", 0, 11, 5)
    air_quality_index = st.sidebar.slider("Air Quality Index", 0, 500, 100)

    user_data = {
        "avg_temp_c": avg_temp_c,
        "precipitation_mm": precipitation_mm,
        "uv_index": uv_index,
        "air_quality_index": air_quality_index,

    }
    features = pd.DataFrame(user_data, index=[0])
    return features

input_df = get_user_input()

if st.button("Predict Dengue Cases"):
    feature_order = ["avg_temp_c", "precipitation_mm", "uv_index", "air_quality_index"]
    input_df = input_df[feature_order]  # Ensure correct order
    
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)
    
    st.subheader("Predicted Dengue Cases")
    st.write(f"{int(prediction[0])} cases")
    st.write("⚠️ Note: This is an approximate prediction. Actual cases may vary due to many factors outside the model's scope.")
