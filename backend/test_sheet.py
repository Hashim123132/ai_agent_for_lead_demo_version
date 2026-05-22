from app.tools import save_lead_to_sheet

lead = {
    "name": "Ali",
    "phone": "03001234567",
    "car_type": "Corolla",
    "pickup_date": "05-22-26",
    "return_date": "05-25-26",
    "budget": "250",
    "currency": "USD",
}

print(save_lead_to_sheet(lead))
