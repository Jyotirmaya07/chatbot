# AI Chatbot (GUI-Based) 🤖

## 📌 Overview

This project is a **desktop-based AI Chatbot** built using Python and Tkinter. It uses the OpenAI API to generate intelligent responses and provides a simple graphical interface for user interaction.

---

## 🚀 Features

* 🤖 AI-powered chatbot (OpenAI API)
* 💬 Real-time conversation
* 🖥️ GUI using Tkinter
* 🔄 Maintains conversation history
* ⚡ Multithreading (no UI freezing)
* ⌨️ Press Enter to send messages

---

## 🛠️ Tech Stack

* Python
* OpenAI API
* Tkinter (GUI)
* python-dotenv (for environment variables)
* Threading

---

## ⚙️ How It Works

1. User enters a message in the GUI
2. Message is added to conversation history
3. Request is sent to OpenAI API
4. Response is displayed in chat window
5. Conversation continues contextually

---

## ▶️ How to Run

### Step 1: Install dependencies

```bash
pip install openai python-dotenv
```

---

### Step 2: Create `.env` file

```env
OPENAI_API_KEY=your_api_key_here
```

⚠️ Do NOT upload `.env` to GitHub

---

### Step 3: Run the program

```bash
python chatbot.py
```

---

## 📁 Project Structure

```bash
chatbot/
│── chatbot.py
│── .env (not uploaded)
│── .gitignore
│── README.md
```

---

## ⚠️ Important Notes

* API key must be kept secret
* `.env` file is excluded using `.gitignore`
* Requires internet connection
* Rate limits may apply

---

## 🔮 Future Improvements

* Add voice input/output
* Improve UI design
* Add chat history saving
* Use advanced AI models

---

## 👨‍💻 Author

Jyotirmaya Swain
