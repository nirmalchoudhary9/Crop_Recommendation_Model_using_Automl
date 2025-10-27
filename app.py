import streamlit as st
import json
import urllib.request

# ==============================
# Azure Endpoint Configuration
# ==============================
AZURE_URL = "https://crop-recommendation-ws-lujnn.centralus.inference.ml.azure.com/score"
API_KEY = "3YUIeOtvweqdnQjwEdwXyffxxvCszRGVgUJpFeePJfdgfrmkModvJQQJ99BJAAAAAAAAAAAAINFRAZML4YjA"

if not API_KEY:
    st.error("⚠️ Please set your Azure API key in the code before using the app.")

# ==============================
# Streamlit UI
# ==============================
st.set_page_config(page_title="🌾 Crop Recommendation System", page_icon="🌱", layout="centered")

st.title("🌾 Crop Recommendation System (Azure Deployed)")
st.markdown("""
Enter the soil and climate parameters below to get a crop recommendation from your **Azure ML model**.
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

# ==============================
# Azure API Request Function
# ==============================
def get_crop_recommendation(inputs: dict):
    """Send user inputs to Azure endpoint and return the prediction result."""
    body = str.encode(json.dumps(inputs))
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer " + API_KEY
    }

    req = urllib.request.Request(AZURE_URL, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read().decode("utf-8")
        return json.loads(result)
    except urllib.error.HTTPError as error:
        st.error(f"❌ Request failed with status code: {error.code}")
        st.text(error.read().decode("utf8", "ignore"))
        return None
    except Exception as e:
        st.error(f"⚠️ Unexpected error: {e}")
        return None

# ==============================
# Submit Button
# ==============================
if st.button("🌱 Recommend Crop"):
    # Prepare data in the format expected by Azure ML endpoint
    data = {
        "input_data": {
            "columns": ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"],
            "index": [0],
            "data": [[N, P, K, temperature, humidity, ph, rainfall]]
        }
    }

    with st.spinner("Fetching crop recommendation from Azure..."):
        result = get_crop_recommendation(data)

    if result:
        try:
            # Try to extract the crop prediction from result
            prediction = (
                result.get("result")
                or result.get("predictions")
                or result
            )
            st.success(f"✅ Recommended Crop: **{prediction}**")
        except Exception:
            st.json(result)

