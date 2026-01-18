import base64
from langchain_ollama import OllamaLLM

def get_image_summary(image_path):
    with open(image_path, "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode("utf-8")
    
    # Use Moondream because it works on your 4GB RAM
    model = OllamaLLM(model="moondream")
    prompt = "Read this image carefully. Transcribe every day of the week and the specific gym routine listed for each day."
    
    # This sends the image to Ollama to be "read"
    return model.invoke(prompt, images=[img_base64])