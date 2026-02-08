# 🤖 AI Console Chatbot with Memory

A simple Python-based AI chatbot that runs in the terminal and remembers conversation history.
The bot uses **LangChain** and the **Groq LLM (gpt-oss-20b)** to generate intelligent responses.

This project demonstrates how Large Language Models (LLMs) can be integrated into real applications using Python.


## ✨ Features

* Interactive terminal chatbot
* Remembers previous conversation (context aware)
* Powered by Groq LLM
* Beginner-friendly code structure
* Environment variable based API security



## 🧠 How It Works

The program continuously takes user input from the terminal.
Each message is stored in a `history` list.
The entire conversation history is sent to the LLM so the chatbot can respond with context awareness.


## 🖥️ Demo

Below is the chatbot running in the terminal:

![Chatbot Demo](https://github.com/mayuri-ai06/ai-console-chatbot/blob/main/assets/MEMORYBOT-OUTPUT.png?raw=true)



## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mayuri-ai06/ai-console-chatbot.git
cd ai-console-chatbot
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create .env file

Create a file named `.env` and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

### 4️⃣ Run the chatbot

```bash
python Memory_bot.py
```

---

## 🛠️ Technologies Used

* Python
* LangChain
* Groq LLM
* python-dotenv

---

## 📌 Learning Outcome

This project helps understand:

* LLM integration in Python
* Conversation memory handling
* Environment variables & API keys
* Terminal based applications

---

## 👩‍💻 Author

**Mayuri Khatarkar**
AIML Student | Python & AI Enthusiast | Graphic Designer
