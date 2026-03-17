# FakeNewsDetector
AI-powered Fake News Detector web app that analyzes news headlines and classifies them as Reliable, Suspicious, or Potentially Misleading using the Groq Llama-3.1-3B model. Built with FastAPI, SQLAlchemy, MySQL, and a clean HTML/CSS/JS frontend, with stored analysis history and intelligent explanations.


# 📰 Fake News Detector

## 📌 Overview

This project is a web-based application that detects whether a news headline is **real or fake** using an AI-powered backend.
It provides a simple interface where users can input a headline and get instant analysis.

---

## 🚀 Features

* Detects fake vs real news headlines
* Fast API-based backend using AI
* Simple and responsive frontend
* Easy integration with external AI models

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Pydantic
* SQLAlchemy

### Frontend

* HTML
* CSS
* JavaScript

### AI Integration

* Groq API (LLM-based analysis)

---

## 📂 Project Structure

```
FakeNewsDetector/
│
├── Backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   ├── ai_service.py
│   └── routers/
│       └── headline.py
│
├── Frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
├── README.md
└── .env.example
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/vinit6969/FakeNewsDetector.git
cd FakeNewsDetector
```

---

### 2. Create virtual environment

```bash
python -m venv myenv
myenv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy pymysql python-dotenv
```

---

### 4. Setup environment variables

Create a `.env` file in the root:

---

### 5. Run the backend

```bash
uvicorn Backend.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

### 6. Run frontend

Open `Frontend/index.html` in your browser.

---

## 📡 API Endpoints

### Detect News

```
POST /analyze
```

**Request Body:**

```json
{
  "headline": "Your news headline here"
}
```

**Response:**

```json
{
  "result": "Fake"
}
```

---

## 🔐 Security Note

* `.env` file is ignored to protect API keys
* Never expose your API keys in public repositories

---

## 📈 Future Improvements

* Add user authentication
* Store analysis history
* Improve AI accuracy with better models
* Deploy as a full-stack web app

---

## 👨‍💻 Author

**Vinit Nikure**

