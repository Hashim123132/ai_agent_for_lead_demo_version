import os
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")