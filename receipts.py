from fastapi import APIRouter, HTTPException, status
from api.models import Receipt
from api.schemas import ReceiptSchema, ReceiptPointsSchema
from api.services import ReceiptService

router = APIRouter()
receipt_service = ReceiptService()

@router.post("/process", status_code=201, response_model=ReceiptSchema)
async def process_receipt(receipt: Receipt):
    try:
        return receipt_service.process_receipt(receipt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing receipt: {e}")

@router.get("/{receipt_id}/points", response_model=ReceiptPointsSchema)
async def get_receipt_points(receipt_id: str):
    try:
        return receipt_service.get_receipt_points(receipt_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) 