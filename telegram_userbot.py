import os
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient, events
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Configuration
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "my_userbot")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ALLOWED_USER_ID = os.getenv("ALLOWED_USER_ID")

# Validation
if not all([API_ID, API_HASH, GROQ_API_KEY, ALLOWED_USER_ID]):
    print("Error: Please set API_ID, API_HASH, GROQ_API_KEY, and ALLOWED_USER_ID in .env file.")
    exit(1)

try:
    ALLOWED_USER_ID = int(ALLOWED_USER_ID)
except ValueError:
    print("Error: ALLOWED_USER_ID must be an integer.")
    exit(1)

# Initialize LLM
try:
    # Model name from Memory_bot.py
    llm = ChatGroq(model="openai/gpt-oss-20b", api_key=GROQ_API_KEY)
except Exception as e:
    print(f"Error initializing ChatGroq: {e}")
    exit(1)

# Initialize Telegram Client
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# Chat History Storage: {chat_id: [("user", "msg"), ("ai", "msg")]}
# Note: In-memory storage. Will be lost on restart.
chat_histories = {}

@client.on(events.NewMessage)
async def handler(event):
    # Check if the sender is the allowed user
    # logic:
    # We want to respond if the message comes FROM the allowed user.
    # We generally ignore our own outgoing messages unless ALLOWED_USER_ID is self and we want to trigger on self.

    sender_id = event.sender_id

    # If the sender is not the allowed user, ignore.
    if sender_id != ALLOWED_USER_ID:
        return

    # We only want to process text messages
    if not event.text:
        return

    chat_id = event.chat_id

    # Initialize history for this chat if not exists
    if chat_id not in chat_histories:
        chat_histories[chat_id] = []

    history = chat_histories[chat_id]

    # User message
    user_message = event.text

    # Append to history
    # LangChain ChatGroq expects list of (role, content) tuples or BaseMessages.
    # Using format from Memory_bot.py
    history.append(("user", user_message))

    try:
        # Indicate typing (optional, but good UX)
        async with client.action(chat_id, 'typing'):
            # Invoke LLM
            # We use ainvoke for async execution to avoid blocking the event loop
            if hasattr(llm, 'ainvoke'):
                response = await llm.ainvoke(history)
            else:
                # Fallback to sync invoke in a thread
                response = await asyncio.to_thread(llm.invoke, history)

            ai_response = response.content

            # Update history
            history.append(("ai", ai_response))

            # Reply
            await event.reply(ai_response)

    except Exception as e:
        print(f"Error generating response: {e}")
        # Optionally reply with error (uncomment if debug needed)
        # await event.reply(f"Error: {str(e)}")

print("Starting Userbot...")
print(f"Listening for messages from User ID: {ALLOWED_USER_ID}")

# Start the client
# This will prompt for phone number/code in the terminal if session is not present
client.start()
client.run_until_disconnected()
