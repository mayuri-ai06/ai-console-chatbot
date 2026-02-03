# ai-console-chatbot# AI Console Chatbot with Memory

This project is a simple console-based AI chatbot built using Python, LangChain, and the Groq LLM (gpt-oss-20b).
The chatbot maintains conversation history, allowing it to generate context-aware responses in an interactive
terminal environment.

## Features
- Interactive chatbot running in the terminal
- Maintains conversation memory using message history
- Built with LangChain and Groq LLM
- Beginner-friendly and easy to extend

## How It Works
The chatbot continuously takes user input from the terminal, stores both user and AI messages in a history list,
and sends the entire conversation context to the language model to generate meaningful responses.

## Demo
Below is a screenshot showing the chatbot running successfully in the terminal:

![Chatbot Demo](https://github.com/mayuri-ai06/ai-console-chatbot/blob/main/MEMORYBOT-OUTPUT.png?raw=true)

## How to Run
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Create a `.env` file and add your Groq API key:
   GROQ_API_KEY=your_api_key_here
4. Run the chatbot:
   python Memory_bot.py
