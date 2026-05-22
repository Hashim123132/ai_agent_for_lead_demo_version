from twilio.twiml.messaging_response import MessagingResponse
from fastapi import APIRouter, Form, Response
from app.agent import chat_with_agent

router = APIRouter()


@router.post("/whatsapp")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    user_message = Body
    user_phone = From

    print("WhatsApp message from:", user_phone)
    print("Message:", user_message)

    ai_reply = chat_with_agent(user_message)

    response = MessagingResponse()
    response.message(ai_reply)

    return Response(
        content=str(response),
        media_type="application/xml"
    )