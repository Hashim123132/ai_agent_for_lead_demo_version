from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.whatsapp import router as whatsapp_router
from app.schemas import ChatRequest, ChatResponse
from app.agent import chat_with_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(whatsapp_router)


@app.get("/")
def root():
    return {"message": "AI Rental Agent backend is running"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = chat_with_agent(request.session_id, request.message)
    return ChatResponse(response=reply)