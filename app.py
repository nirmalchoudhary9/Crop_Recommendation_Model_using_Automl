import streamlit as st
import pandas as pd
import pickle

# ----------------------------
# Load your trained model
# ----------------------------
MODEL_PATH = "crop_model.pkl"   # update this if your model is elsewhere
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# ----------------------------
# Streamlit App UI
# ----------------------------
st.set_page_config(page_title="🌾 Crop Recommendation System", page_icon="🌱", layout="centered")

st.title("🌾 Crop Recommendation System")
st.markdown("""
Enter the soil and climate parameters below to get the best crop recommendation.
""")

# Input fields
col1, col2, col3 = st.columns(3)
with col1:
    N = st.number_input("Nitrogen (N)", min_value=0.0, step=1.0)
    P = st.number_input("Phosphorus (P)", min_value=0.0, step=1.0)
    K = st.number_input("Potassium (K)", min_value=0.0, step=1.0)
with col2:
    temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)
    humidity = st.number_input("Humidity (%)", min_value=0.0, step=0.1)
with col3:
    ph = st.number_input("pH value", min_value=0.0, max_value=14.0, step=0.1)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1)

# Prediction button
if st.button("🌱 Recommend Crop"):
    # Prepare input for prediction
    input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                              columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

    try:
        prediction = model.predict(input_data)[0]
        st.success(f"✅ Recommended Crop: **{prediction.upper()}**")
    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")

