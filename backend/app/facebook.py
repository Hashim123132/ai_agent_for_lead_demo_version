from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

from app.agent import chat_with_agent
from app.config import VERIFY_TOKEN
from app.facebook_client import send_facebook_message

router = APIRouter()


@router.get("/facebook/webhook")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(content=challenge)

    return {"error": "Invalid token"}


@router.post("/facebook/webhook")
async def receive_message(request: Request):
    data = await request.json()
    print("Facebook webhook data:", data)

    for entry in data.get("entry", []):
        for event in entry.get("messaging", []):
            sender_id = event["sender"]["id"]

            if "message" in event and "text" in event["message"]:
                user_message = event["message"]["text"]

                try:
                    ai_reply = chat_with_agent(sender_id, user_message)
                except Exception as e:
                    print("AI error:", e)
                    ai_reply = "Sorry, AI is busy right now. Please try again."

                send_facebook_message(sender_id, ai_reply)

    return {"status": "ok"}