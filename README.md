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
- OpenAPI account with API Key

## Setup Instructions:

1. **Clone the Repository:**

```bash
git clone https://github.com/leartallushaj96/openai-qa-task.git
cd openai-qa-task

2. **Install Dependencies:**
pip install -r requirements.txt

3. **Configure API Key:**
Create a .env file in the root directory.
OPENAI_API_KEY=your-openai-api-key-here
ROUTER_API_KEY=your-openrouter-api-key-here
(You can get your API key from OpenRouter)


Running the Project:
Run OpenAI Official API Integration:

Command : python scr/open-ai.py
Sends 20 questions (or allows custom questions).

Saves results to openapi-responses.json.

Logs to open-ai.log.

Run OpenRouter API Integration:

Command : python src/api-router.py
Sends 20 questions (or allows custom questions).

Saves results to api-router-responses.json.

Logs to api-router.log.



