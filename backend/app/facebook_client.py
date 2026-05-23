import requests
from app.config import PAGE_ACCESS_TOKEN


def send_facebook_message(recipient_id: str, message_text: str):
    url = "https://graph.facebook.com/v19.0/me/messages"

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }

    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }

    response = requests.post(url, params=params, json=payload)
    print("Facebook send response:", response.status_code, response.text)