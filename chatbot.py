import openai
import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import scrolledtext, END
import threading

# Load OpenAI API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

conversation_history = []

# Function to handle sending messages
def send_message():
    user_message = user_input.get()
    if not user_message.strip():
        return

    chat_window.insert(END, f"You: {user_message}\n")
    user_input.delete(0, END)

    conversation_history.append({"role": "user", "content": user_message})

    def get_bot_response():
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation_history,
                max_tokens=500,
                temperature=0.7
            )
            bot_reply = response['choices'][0]['message']['content']
            conversation_history.append({"role": "assistant", "content": bot_reply})
            chat_window.insert(END, f"Bot: {bot_reply}\n\n")
            chat_window.see(END)

        except openai.error.RateLimitError:
            chat_window.insert(END, "🚨 Rate limit exceeded. Try again later.\n\n")
        except Exception as e:
            chat_window.insert(END, f"❗ Error: {e}\n\n")

    # Run API call in a thread to avoid freezing UI
    threading.Thread(target=get_bot_response).start()

# GUI setup
root = tk.Tk()
root.title("AI Chatbot")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Arial", 12))
chat_window.pack(padx=10, pady=10)
chat_window.config(state=tk.NORMAL)

user_input = tk.Entry(root, width=70, font=("Arial", 12))
user_input.pack(padx=10, pady=5, side=tk.LEFT)

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(padx=5, pady=5, side=tk.LEFT)

def handle_enter_key(event):
    send_message()

user_input.bind("<Return>", handle_enter_key)

chat_window.insert(END, "🤖 ChatGPT Bot Ready! Type your message below.\n\n")

root.mainloop()
