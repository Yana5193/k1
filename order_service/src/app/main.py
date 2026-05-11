import os
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Order Service")

# Адреса сервисов
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://product-service:8000")
DISCOUNT_SERVICE_URL = os.getenv("DISCOUNT_SERVICE_URL", "http://discount-service:8000")

class OrderRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    promo_code: str = None 

class ProductFromService(BaseModel):
    id: str
    name: str
    price: float
    available: bool

@app.post("/orders")
async def create_order(order: OrderRequest):
    product = await fetch_product(order.product_id)

    if not product.available:
        raise HTTPException(
            status_code=400,
            detail=f"Product '{order.product_id}' is not available",
        )
    async with httpx.AsyncClient(timeout=3.0) as client:
        try:
            d_resp = await client.post(
                f"{DISCOUNT_SERVICE_URL}/discounts/calculate",
                json={
                    "product_id": order.product_id,
                    "quantity": order.quantity,
                    "price": product.price,
                    "promo_code": order.promo_code
                }
            )
            d_resp.raise_for_status()
            discount_data = d_resp.json()
        except Exception:
            discount_data = {"discount_percent": 0, "reason": "Service unavailable"}

    # 3. Считаем итог
    pct = discount_data["discount_percent"]
    total_before = product.price * order.quantity
    discount_amount = total_before * (pct / 100)
    final_price = total_before - discount_amount

    return {
        "product_id": product.id,
        "quantity": order.quantity,
        "unit_price": product.price,
        "total_before_discount": total_before,
        "discount_percent": f"{pct}%",
        "discount_amount": discount_amount,
        "final_price": final_price,
        "reason": discount_data["reason"]
    }

async def fetch_product(product_id: str) -> ProductFromService:
    url = f"{PRODUCT_SERVICE_URL}/products/{product_id}"
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(url)
            if response.status_code == 404:
                raise HTTPException(status_code=404, detail="Product not found")
            response.raise_for_status()
            return ProductFromService.model_validate(response.json())
    except httpx.RequestError as exc:
        raise HTTPException(status_code=503, detail=f"Service unavailable: {exc}")