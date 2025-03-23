import openai
import os
from dotenv import load_dotenv
import json

# Load API key from .env
load_dotenv()
api_key = os.getenv('ROUTER_API_KEY')

client = openai.OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

#list of questions 
questions = [
    "Which is the biggest city in Europe?",
    "Can you give me two websites where to read books?",
    "Who is the writer of Harry Potter book?",
    "Which is the longest tunnel in Europe?",
    "How many years old is albanian language",
    "How many is the population of Tirana?",
    "Which is albanian national currency?",
    "Who is the most famous singer in Albania?",
    "Translate 'hello' to Albanian.",
    "Who discovered America?",
    "What is the speed of Ferrari?",
    "What is chatgpt?",
    "Who is Donald Trump?",
    "Who is Fernando Alonso?",
    "Who is Leonardo Da Vinci?",
    "Which is the most used social network in Europe?",
    "Give me a fish based recipse",
    "What’s the longest river in Albania?",
    "How many oceans are there?",
    "What is an API integration?"
]


responses = []


for idx, question in enumerate(questions):
    print(f"Sending Question {idx+1}: {question}")

    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )

        reply = response.choices[0].message.content.strip()

        print(f"Response: {reply}\n")

        # Store question & answer
        responses.append({
            "question": question,
            "response": reply
        })

    except Exception as e:
        print(f"Error for question '{question}': {e}")
        responses.append({
            "question": question,
            "response": "Error occurred"
        })

#Save responses to JSON file
with open("api-router-responses.json", "w", encoding="utf-8") as f:
    json.dump(responses, f, ensure_ascii=False, indent=4)

print("All responses are saved properly as json")