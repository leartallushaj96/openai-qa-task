import openai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv('OPENROUTER_API_KEY')

client = openai.OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


response = client.chat.completions.create(
    model="openai/gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello! Do you speak albanian?"}]
)

print("ChatGPT Reply:", response.choices[0].message.content)
