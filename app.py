import streamlit as st
import requests
import json

# Headers for request
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Streamlit UI
st.title("Azure ML Model Deployment with Streamlit")
st.subheader("Enter the input data for prediction")

# Example input form
input_data = st.text_area("Enter input data in JSON format:", "{}")

# Prediction button
if st.button("Predict"):
    try:
        # Convert input to JSON
        payload = json.loads(input_data)

        # Send request to Azure ML Endpoint
        response = requests.post(AZURE_ENDPOINT, headers=HEADERS, json=payload)

        # Display Results
        if response.status_code == 200:
            st.success("Prediction Successful!")
            result = response.json()
            st.json(result)
        else:
            st.error(f"Request failed with status code {response.status_code}")
            st.text(response.text)
    
    except json.JSONDecodeError:
        st.error("Invalid JSON input. Please enter valid JSON data.")

