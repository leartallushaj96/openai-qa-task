# OpenAI API Integration
This project demonstrates how to integrate with the OpenAI API (via OpenRouter) to send multiple queries, handle the responses, and store the data in JSON format.

## Features

- Integration with OpenAI API using OpenRouter.
- Sends 20 predefined questions to the model.
- Saves both questions and responses into a JSON file.
- Uses `.env` to securely store API keys.


### Prerequisites:

- Python 3.x installed.
- OpenRouter account with API key (free, no credit card required).

## Setup Instructions:

1. **Clone the Repository:**

```bash
git clone https://github.com/leartallushaj96/openai-qa-task.git
cd openai-qa-task

2. **Install Dependencies:**
pip install -r requirements.txt

3. **Configure API Key:**
Create a .env file in the root directory.
(You can get your API key from OpenRouter)
OPENROUTER_API_KEY=your-api-key-here

Running the Project:
python main.py

The script will send 20 questions to the API.
Responses will be saved in responses.json