# AssistIQ – AI Powered Customer Support Assistant

## Overview

AssistIQ is an AI-powered customer support system that enables organizations to build a searchable knowledge base from company documents. Users can upload PDF, DOCX, and TXT files and ask questions based on the uploaded content through an interactive chat interface.

---

## Features

- Upload PDF, DOCX and TXT documents
- Build a centralized knowledge base
- AI-powered question answering
- Document management dashboard
- Modern React frontend
- FastAPI backend
- SQLite database
- ChromaDB vector storage
- SentenceTransformer embeddings
- Swagger API documentation

---

## Tech Stack

### Frontend
- React
- Vite
- Axios

### Backend
- FastAPI
- Python
- SQLAlchemy
- SQLite
- ChromaDB
- Sentence Transformers

---

## Project Structure

```
AssistIQ
│
├── backend
│   ├── app
│   ├── storage
│   ├── main.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## Installation

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /upload | Upload company documents |
| POST | /chat | Ask questions |
| GET | /documents | View uploaded documents |
| GET | /stats | Dashboard statistics |
---
## Future Improvements

- Multi-user authentication
- Conversation history
- Better semantic retrieval
- Cloud deployment
- Advanced analytics

---

## Author

Anisha Sharma