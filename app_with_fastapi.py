import requests
import streamlit as st

# Streamlit layout
st.title("CIFAR10 Prediction")

HOST = "http://localhost:8000"

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    with st.container(height=300):
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    if st.button('Predict'):
        # Send image to FastAPI endpoint
        files = {'file': uploaded_file}
        response = requests.post(f"{HOST}/upload_image_for_inference", files=files)

        if response.status_code == 200:
            result = response.json()
            st.header(f"Predicted Label: {result['predicted_class']}")
        else:
            st.error("Error processing image. Please try again.")

