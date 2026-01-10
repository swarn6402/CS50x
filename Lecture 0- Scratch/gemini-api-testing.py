import os
from google import genai

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model = "gemini-2.0-flash",
    contents = "Explain me what is CS50 in one sentence"
)
print (response.text)