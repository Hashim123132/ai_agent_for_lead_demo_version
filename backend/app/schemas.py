from pydantic import BaseModel
from typing import Optional
class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    response: str

class LeadData(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    car_type: Optional[str] = None
    pickup_date: Optional[str] = None
    return_date: Optional[str] = None
    budget: Optional[str] = None
    currency: Optional[str] = "USD"