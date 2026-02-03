from dotenv import load_dotenv

load_dotenv()
from langchain_groq import ChatGroq

llm= ChatGroq (model="openai/gpt-oss-20b")

history= []

while True:
    query = input("user:")
    history.append(("user", query))
    res= llm.invoke(history)
    history.append(("ai",res.content))
    print(f"Bot: {res.content}\n")