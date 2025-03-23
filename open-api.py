import openai
import os
from dotenv import load_dotenv
import json
import time
from openai import RateLimitError, APIError, Timeout, AuthenticationError, BadRequestError

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI(api_key=api_key)

default_questions = [
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

use_custom = input("Do you want to input your own questions? (yes/no): ").strip().lower()

if use_custom == 'yes':
    questions = []
    print("Enter your questions one by one. Type 'done' when finished:")
    while True:
        user_input = input("Enter question: ")
        if user_input.lower() == 'done':
            break
        if user_input.strip() != '':
            questions.append(user_input.strip())
    if not questions:
        print("No custom questions entered. Using default questions.")
        questions = default_questions
else:
    questions = default_questions

responses = []

for idx, question in enumerate(questions):
    print(f"Sending Question {idx+1}: {question}")

    while True:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}]
            )
            reply = response.choices[0].message.content.strip()
            print(f"Response: {reply}\n")

            responses.append({
                "question": question,
                "response": reply
            })
            break

        except RateLimitError:
            print(f"Rate limit hit for Question {idx+1}. Waiting 10 seconds...")
            time.sleep(10)

        except (APIError, Timeout) as e:
            print(f"Temporary API Error: {e}. Retrying in 5 seconds...")
            time.sleep(5)

        except AuthenticationError as e:
            print(f"Authentication Error: {e}. Check your API Key.")
            exit(1)

        except BadRequestError as e:
            print(f"Invalid Request Error: {e}. Skipping this question.")
            responses.append({
                "question": question,
                "response": "Invalid Request Error occurred"
            })
            break

        except Exception as e:
            print(f"Unexpected Error for Question {idx+1}: {e}")
            responses.append({
                "question": question,
                "response": "Unexpected Error occurred"
            })
            break

with open("openapi-responses.json", "w", encoding="utf-8") as f:
    json.dump(responses, f, ensure_ascii=False, indent=4)

print("All responses saved successfully to openapi-responses.json")
