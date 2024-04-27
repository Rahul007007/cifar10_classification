from PIL import Image
import streamlit as st
import requests
import model

# Streamlit layout
st.title("CIFAR10 Prediction")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert uploaded file to PIL image
    image = Image.open(uploaded_file)
    
    # Display the uploaded image
    with st.container(height=300):
        st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button('Predict'):
        predicted_class = model.predict(image)

        if predicted_class is not None:
            st.header(f"Predicted Label: {predicted_class}")
        else:
            st.error("Error processing image. Please try again!")
