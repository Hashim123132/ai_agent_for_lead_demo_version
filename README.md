

ai-rental-agent/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app
│   │   ├── agent.py             # LangChain agent logic
│   │   ├── prompts.py           # agent instructions
│   │   ├── tools.py             # Google Sheet tool
│   │   ├── schemas.py           # request/response models
│   │   └── config.py            # env variables
│   ├── requirements.txt
│   └── .env
└── frontend/
    └── simple chat UI



    frontend/src/
├── components/
│   ├── Sidebar.tsx
│   ├── ChatWindow.tsx
│   └── ChatInput.tsx
├── pages/
│   └── Home.tsx
├── App.tsx
└── index.css


COMMANDS

FOR BACKEND

cd /media/DATA/ai-rental-agent/backend
source .venv/bin/activate
uvicorn app.main:app --reload



credential.JSON 

YOU WILL GET THIS from google cloud console