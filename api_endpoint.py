import os
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
from PIL import Image
import model

app = FastAPI()
# Add the CORSMiddleware to enable Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload_image_for_inference") # This is the endpoint for updating the bot's Knowledge Base
async def upload_image(file: UploadFile = File(...)):
    # Save the uploaded image to a file
    with open('image.jpg', 'wb') as image:
        contents = await file.read()  # Read the content of the uploaded file
        image.write(contents)  # Write the content to the image file

    # Process the image
    image_pil = Image.open('image.jpg')  # Open the image using PIL

    # Predict the image class
    predicted_class = model.predict(image_pil)
    # print(f"Predicted label: {predicted_class}")

    image_pil.close()
    # Delete the image file after processing
    os.remove("image.jpg")

    return {'predicted_class': predicted_class}