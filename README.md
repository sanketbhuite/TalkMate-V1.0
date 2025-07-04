# 🎙️ TalkMate v1.0 – Friendly AI English Tutor

**TalkMate** is a web-based virtual English tutor that helps users improve their spoken English by having natural conversations. It listens to your speech, corrects mistakes, gives grammar tips, and replies like a real friend.

---

## ✨ Features

- 🎤 **Voice-to-Text Input** (Web Speech API)
- 🤖 **Natural English Conversations** with AI
- ✍️ **Grammar Correction + Tips**
- 🧠 **Casual, Friendly Tone** like your best English buddy
- 💬 **JSON-based Response Handling**

---

## 📁 Project Structure

```
TalkMate/
├── static/
│   └── logoimg.png
│   └── style.css          # Styling (optional)
├── templates/
│   └── index.html          # Frontend HTML + JS
├── app.py                  # Flask backend logic
├── utils.py                  # Flask backend logic
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## ⚙️ Setup Instructions

### 1. 📥 Clone the repo
```bash
git clone https://github.com/sanketbhuite/TalkMate-v1.0.git
cd TalkMate
```

### 2. 📦 Install Requirements
Make sure Python is installed and run:
```bash
pip install -r requirements.txt
```

> ⚠️ If pip isn’t recognized, check if Python is installed and added to PATH.

### 3. 🔑 Set Your API Key
You can use [OpenRouter](https://openrouter.ai/) or [OpenAI](https://platform.openai.com/account/api-keys).

Create a `.env` file (or set environment variables):

```env
OPENAI_API_KEY=your_key_here
OPENAI_API_BASE=https://openrouter.ai/api/v1
```

Or directly in terminal (for testing):

```bash
export OPENAI_API_KEY=your_key_here
export OPENAI_API_BASE=https://openrouter.ai/api/v1
```

---

## 🚀 Run the App

```bash
python app.py
```

Open your browser and visit:
```
http://localhost:5000
```

---

## 🧪 How to Use

1. Click **"🎤 Start Talking"**
2. Speak a sentence in English
3. TalkMate will:
   - Reply like a friend
   - Correct your sentence (if needed)
   - Give a grammar tip (if needed)
   - Speak the reply out loud

---

## 🧠 Developer Info

TalkMate is created with ❤️ by **Sanket Shivaji Bhuite**, a passionate Computer Science student from Sangola, Maharashtra 🇮🇳 — trained and tuned with help from **ChatGPT**.

---

## 🚧 Next Version (v2.0 Sneak Peek)

- 🧠 Full conversation memory
- 🗣️ More natural, flowing dialogue
- conversation pdf at end

---

## 📃 License

This project is for educational/demo purposes. Feel free to modify and build upon it!

---

> Let's Talk English. Let's TalkMate. 💬✨
