import os
from google import genai

client = genai.Client(api_key = os.getenv("AIzaSyDmtGPH_i6mrM6xK0BCXAWZu0LYgKsK8u8"))

response = client.models.generate_content(
    model = "gemini-2.0-flash",
    contents = "Say exactly : Gemini SDK is working!"
)

print (response.text)
