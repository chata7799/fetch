from pydantic import BaseModel

class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: list[dict]
    total: float