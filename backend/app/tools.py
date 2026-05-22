from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from app.config import GOOGLE_SHEET_ID

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def save_lead_to_sheet(lead: dict):
    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=SCOPES
    )

    service = build("sheets", "v4", credentials=creds)

    values = [[
        lead.get("name"),
        lead.get("phone"),
        lead.get("car_type"),
        lead.get("pickup_date"),
        lead.get("return_date"),
        lead.get("budget"),
        lead.get("currency"),
        "New Lead"
    ]]

    service.spreadsheets().values().append(
        spreadsheetId=GOOGLE_SHEET_ID,
        range="Sheet1!A:H",
        valueInputOption="USER_ENTERED",
        body={"values": values}
    ).execute()

    return "Lead saved"