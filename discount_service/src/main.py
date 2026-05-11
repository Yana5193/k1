from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DiscountRequest(BaseModel):
    product_id: str
    quantity: int
    price: float
    promo_code: str = None

@app.post("/discounts/calculate")
async def calculate_discount(req: DiscountRequest):
    discount_percent = 0
    reason = "No discount"

    # Логика промокода
    if req.promo_code == "STUDENT10":
        discount_percent = 10
        reason = "Student promo code"
    # Логика опта
    elif req.quantity >= 10:
        discount_percent = 15
        reason = "Bulk discount"

    return {
        "discount_percent": discount_percent, 
        "reason": reason
    }