---
title: Cifar10 Classification
emoji: 🤗
colorFrom: red
colorTo: pink
sdk: streamlit
sdk_version: 1.33.0
app_file: app.py
pinned: false
license: apache-2.0
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


### To access the app, follow these steps:


Step 1: Access the app directly on the link (This does not use the FastAPI endpoints):
[https://huggingface.co/spaces/TrishanuDas/cifar10_classification](https://huggingface.co/spaces/TrishanuDas/cifar10_classification)

Step 2: Use the Streamlit app via the FastAPI endpoint.(This could not be deployed due to non-accessibility of a non-crashable server like an AWS ec2 instance) 
- Run the FastAPI server on any instance using the following command:
    ```
    uvicorn api_endpoint:app --reload --host <host_name>
    ```
- Change the HOST variable on the `app_with_fastapi.py` file.
- Execute the app_with_fastapi.py file using the following command:
    ```
    streamlit run app_with_fastapi.py
    ```

### Files

The following files are present in this repository:

- `app.py`: The main Streamlit app file to run directly.
- `requirements.txt`: The list of Python dependencies required by the app.
- `model.py`: Contains the code for loading and using the pre-trained model.
- `app_endpoint.py`: Contains api_endpoint for the prediction.
- `app_with_fastapi.py`: Contains the code for the Streamlit app with FastAPI endpoint.
