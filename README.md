<h1 align="center">chatbot: Powered by Free LLM APIs</h1>

<p align="center" style="margin-top:30px;">
  <img src="https://www.shutterstock.com/image-vector/chat-bot-icon-virtual-smart-600nw-2478937555.jpg" height="200cm"/>
</p>

<p align="center">Minimal terminal chatbot that lets you talk to free LLMs via OpenRouter — pick a LLM ID and start chatting.</p>

### Getting Started: API Key + Run
1. Go to [OpenRouter](https://openrouter.ai) 
2. Create an account  
3. Navigate to [Settings](https://openrouter.ai/settings/preferences) 
4. Click on [Keys](https://openrouter.ai/settings/keys) 
5. Select Create API Key
6. Enter the name you want to save the key with (e.g. "API Key")
7. Fork and clone the repoistory by running the below command in the terminal:
   ```
   git clone https://github.com/kr1shnasomani/chatbot.git
   cd chatbot
   ```
   
8. Paste your OpenRouter API key in `main.py` (line 3)
9. Select a LLM's "id" from the `free-models.json` and paste it into `main.py` (line 4)
10. Now run the `main.py` script and you will be able to talk to your chatbot in the terminal

<br>

> The data for the free LLM APIs is being extracted from [OpenRouter](https://openrouter.ai/models?max_price=0). The data extracted from this link is stored in the `free-models.json` file.

### List of Large Language Model Providers:
- Google
- OpenAI
- Qwen
- MoonshotAI
- Mistral
- DeepSeek
- Meta (Llama)
- NVIDIA
- Microsoft
- Reka
- Tencent
- Sarvam AI
- TNG Tech
- Cognitive Computations
- Venice.ai
- Nous Research
- ArliAI
- Agentica
- Shisa AI