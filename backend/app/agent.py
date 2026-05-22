from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from datetime import datetime
import json
import re

from app.prompts import SYSTEM_PROMPT, EXTRACT_LEAD_PROMPT
from app.config import MISTRAL_API_KEY
from app.tools import save_lead_to_sheet

llm = ChatMistralAI(
    model="mistral-small-latest",
    api_key=MISTRAL_API_KEY,
    temperature=0
)

sessions = {}
leads = {}
saved_leads = set()


def clean_phone(value):
    if not value:
        return None

    phone = str(value).strip()
    digits = re.sub(r"\D", "", phone)

    if len(digits) < 10:
        return None

    return phone


def create_empty_lead():
    return {
        "name": None,
        "phone": None,
        "car_type": None,
        "pickup_date": None,
        "return_date": None,
        "budget": None,
        "currency": "USD",
    }


def extract_lead_from_chat(session_id: str):
    messages_text = "\n".join(
        [f"{type(msg).__name__}: {msg.content}" for msg in sessions[session_id]]
    )
    extract_prompt = EXTRACT_LEAD_PROMPT.format(
        messages_text=messages_text
    )

    response = llm.invoke([HumanMessage(content=extract_prompt)])

    try:
        return json.loads(response.content)
    except Exception:
        return create_empty_lead()


def is_lead_complete(lead: dict):
    required_fields = [
        "name",
        "phone",
        "car_type",
        "pickup_date",
        "return_date",
        "budget",
    ]

    return all(lead.get(field) for field in required_fields)


def chat_with_agent(session_id: str, message: str) -> str:
    today = datetime.now().strftime("%m-%d-%y")
    system_prompt = SYSTEM_PROMPT.format(today=today)

    if session_id not in sessions:
        sessions[session_id] = [SystemMessage(content=system_prompt)]
        leads[session_id] = create_empty_lead()

    sessions[session_id].append(HumanMessage(content=message))

    response = llm.invoke(sessions[session_id])
    sessions[session_id].append(AIMessage(content=response.content))

    extracted_lead = extract_lead_from_chat(session_id)

    for key, value in extracted_lead.items():
        if key not in leads[session_id] or not value:
            continue

        if key == "phone":
            value = clean_phone(value)
            if not value:
                continue

        leads[session_id][key] = value

    if is_lead_complete(leads[session_id]) and session_id not in saved_leads:
        save_lead_to_sheet(leads[session_id])
        saved_leads.add(session_id)
        

        return response.content + "\n\nYour rental inquiry has been saved successfully."

    return response.content