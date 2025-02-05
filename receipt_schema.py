from pydantic import BaseModel

class ReceiptSchema(BaseModel):
    id: str

class ReceiptPointsSchema(BaseModel):
    points: int 