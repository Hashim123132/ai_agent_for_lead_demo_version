# AI Rental Inquiry Agent

<p align="center">
  <img src="./assets/ree;37.gif" width="900">
</p>

## Features

- AI rental assistant
- Natural conversation
- Lead extraction
- Google Sheets integration
- Session memory
- Facebook Messenger support
- FastAPI backend
- React frontend
## FOLDER STRUCTURE

ai-rental-agent/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app entry point
│   │   ├── agent.py             # AI agent logic
│   │   ├── prompts.py           # System prompts
│   │   ├── tools.py             # Google Sheets tools
│   │   ├── schemas.py           # Request/response models
│   │   ├── config.py            # Environment variables
│   │   └── __init__.py
│   │
│   ├── credential.json          # Google service account credentials
│   ├── requirements.txt
│   ├── .env
│   └── .venv/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Sidebar.tsx
│   │   │   ├── ChatWindow.tsx
│   │   │   └── ChatInput.tsx
│   │   │
│   │   ├── pages/
│   │   │   └── Home.tsx
│   │   │
│   │   ├── App.tsx
│   │   └── index.css
│   │
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
│
├── assets/
│   ├── demo.gif
│   └── lead-capture.gif
│
├── README.md
└── LICENSE






## Tech Stack

- FastAPI
- LangChain
- Mistral AI
- React
- Google Sheets API

## Project Structure

(project tree)

## Setup

### Backend

cd backend
source .venv/bin/activate
uvicorn app.main:app --reload

### Frontend

npm install
npm run dev

## Google Credentials

Place credential.json inside backend/

Generate from Google Cloud Console.

## Environment Variables

(example .env)

## Future Improvements

- Redis session storage
- WhatsApp integration
- CRM integration
- Analytics dashboard

## License

MIT