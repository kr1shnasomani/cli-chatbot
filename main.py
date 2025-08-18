import requests

API_KEY = "your_openrouter_api_key" # Replace with your actual OpenRouter API key
MODEL = "model_id" # Replace with the actual LLM API ID
URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

while True:
    user_message = input("You: ")
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }
    response = requests.post(URL, headers=HEADERS, json=payload)
    result = response.json()
    if "choices" in result and result["choices"]:
        print("Chatbot:", result["choices"][0]["message"]["content"])
    else:
        print("Chatbot: Error or no response from model.", result)