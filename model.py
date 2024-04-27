from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch

# Loading processor and model
processor = AutoImageProcessor.from_pretrained("heyitskim1912/AML_A2_Q4")
model = AutoModelForImageClassification.from_pretrained("heyitskim1912/AML_A2_Q4")

def predict(image_pil):
    inputs = processor(image_pil, return_tensors="pt")

    #Inference
    with torch.no_grad():
        logits = model(**inputs).logits

    # Get predicted label
    predicted_label = logits.argmax(-1).item()
    predicted_class = model.config.id2label[predicted_label]
    return predicted_class