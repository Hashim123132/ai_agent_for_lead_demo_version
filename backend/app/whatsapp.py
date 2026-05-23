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

    try:
        ai_reply = chat_with_agent(user_phone, user_message)
        print("AI reply:", ai_reply)

        if not ai_reply:
            ai_reply = "Sorry, I could not generate a reply."

    except Exception as e:
        print("AI error:", e)
        ai_reply = "Sorry, AI is busy right now. Please try again."

    response = MessagingResponse()
    response.message(str(ai_reply))

    xml_response = str(response)
    print("XML response:", xml_response)

    return Response(
        content=xml_response,
        media_type="application/xml"
    )