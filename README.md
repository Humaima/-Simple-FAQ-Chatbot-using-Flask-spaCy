# 🤖 Simple FAQ Chatbot using Flask & spaCy

![title_image](https://github.com/user-attachments/assets/6b8c8f4a-4acf-46b5-a900-2740fbe552cb)

This repository contains two versions of a basic chatbot built using Python, Flask, and spaCy:

- ✅ **Version 1**: Chatbot with HTML, CSS, and JavaScript front-end
  
![image](https://github.com/user-attachments/assets/bd77924e-4ba2-4523-9ee9-d5b4992ef5eb) 

![image](https://github.com/user-attachments/assets/91d32f30-3c21-444d-b3fb-04231879b0ed)

- ✅ **Version 2**: Backend-only chatbot tested via Postman, `curl`, or minimal HTML form
  
![image](https://github.com/user-attachments/assets/71554914-6ea4-4525-b448-300bbffeb9c4)

![image](https://github.com/user-attachments/assets/49aac404-efdc-4448-be01-d470937cf13e)

---

## 🧠 Features

- Answer pre-defined FAQ questions
- Fallback response for unknown inputs
- spaCy-powered similarity matching
- Flask API for handling user input

---
## 🔧 Requirements

Make sure you have the following installed:

```bash
pip install flask spacy
python -m spacy download en_core_web_sm
```
---
## 📁 Project Structure
chatbot/
│
├── main.py                 # Main Flask app (backend only version)
├── advanced_app/          # Version with front-end
│   ├── app.py             # Flask app with HTML/CSS/JS
│   ├── responses.py       # FAQ dictionary
│   ├── templates/
│   │   └── index.html     # Web UI
│   └── static/
│       └── style.css      # Styles
└── README.md

## 🚀 Version 1: With HTML, CSS, JS

# ▶️ Run the App

```bash
cd advanced_app
python app.py
```

# Open in Browser
```bash
Visit: http://127.0.0.1:5000
```

# 💬 Features

- Interactive web interface
- Styled chatbox UI
- Real-time conversation using fetch API

## ⚙️ Version 2: Backend-Only (API)

# ▶️ Run the App
```bash
python app.py
```

# 🔁 Test the Chatbot (via curl)
```bash
curl -X POST http://127.0.0.1:5000/chat \
     -H "Content-Type: application/json" \
     -d "{\"msg\": \"what is flask\"}"
```

## 🤖 Sample FAQs (Used Internally)
- "what is your name"
- "how are you"
- "what can you do"
- "bye"
- "hello"
- "what is flask"

## 🧠 How It Works

- User sends a message (msg)
- spaCy computes similarity between input and known questions
- If similarity > 0.7, returns best match; otherwise returns fallback

## 📌 To Do

- Add file/database persistence for FAQs
- Add NLP preprocessing (lemmatization, punctuation handling)
- Enhance UI with animations or avatars

## 📝 License
MIT License. Use freely, just give credit where due.
