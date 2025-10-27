import streamlit as st
import json
import urllib.request

AZURE_URL = "https://crop-recommendation-ws-lujnn.centralus.inference.ml.azure.com/score"
API_KEY = "3YUIeOtvweqdnQjwEdwXyffxxvCszRGVgUJpFeePJfdgfrmkModvJQQJ99BJAAAAAAAAAAAAINFRAZML4YjA"

st.set_page_config(page_title="🌾 Crop Recommendation System", page_icon="🌱", layout="centered")

st.markdown("""
<style>
    .main {
        background-color: #f9fafb;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    h1, h2, h3, h4 {
        color: #2e7d32;
        text-align: center;
        font-weight: 700;
    }
    .stButton>button {
        width: 100%;
        background-color: #2e7d32;
        color: white;
        font-size: 1.1em;
        font-weight: 600;
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #43a047;
        transform: scale(1.02);
    }
    .footer {
        text-align: center;
        font-size: 0.9em;
        color: #777;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌾 Intelligent Crop Recommendation")
st.markdown("""
This system uses an **Azure Machine Learning** model to recommend the most suitable crop  
based on soil nutrients and environmental conditions.
""")

if not API_KEY:
    st.warning("⚠️ Please add your Azure API key in the code before using the app.")


with st.container():
    st.subheader("🧪 Enter Soil and Weather Parameters")

    col1, col2, col3 = st.columns(3)
    with col1:
        N = st.number_input("Nitrogen (N)", min_value=0.0, step=1.0, value=0.0)
        P = st.number_input("Phosphorus (P)", min_value=0.0, step=1.0, value=0.0)
        K = st.number_input("Potassium (K)", min_value=0.0, step=1.0, value=0.0)
    with col2:
        temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1, value=0.0)
        humidity = st.number_input("Humidity (%)", min_value=0.0, step=0.1, value=0.0)
    with col3:
        ph = st.number_input("pH value", min_value=0.0, max_value=14.0, step=0.1, value=0.0)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1, value=0.0)

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

st.markdown("---")
st.subheader("🌱 Get Recommendation")

# Center the button using Streamlit columns
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    predict_btn = st.button("🔍 Recommend Best Crop")

if predict_btn:
    # Prepare JSON data
    data = {
        "input_data": {
            "columns": ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"],
            "index": [0],
            "data": [[N, P, K, temperature, humidity, ph, rainfall]]
        }
    }

    with st.spinner("Fetching prediction from Azure..."):
        result = get_crop_recommendation(data)

    if result:
        try:
            if isinstance(result, dict):
                result_text = str(list(result.values())[0]) if len(result) == 1 else str(result)
            elif isinstance(result, list):
                result_text = str(result[0])
            else:
                result_text = str(result)

            result_text = (
                result_text.replace("[", "")
                .replace("]", "")
                .replace("{", "")
                .replace("}", "")
                .replace("0:", "")
                .replace('"', "")
                .strip()
            )

            st.success(f"✅ **Recommended Crop: {result_text.capitalize()}**")

        except Exception as e:
            st.error(f"⚠️ Could not parse the response: {e}")
            st.json(result)

