from datetime import datetime
from api.models import Receipt
from api.schemas import ReceiptSchema, ReceiptPointsSchema

class ReceiptService:
    def __init__(self):
        self.receipts = {} 

    def process_receipt(self, receipt: Receipt) -> ReceiptSchema:
        receipt_id = str(uuid.uuid4()) 
        points = self._calculate_points(receipt)
        self.receipts[receipt_id] = {'points': points}
        return ReceiptSchema(id=receipt_id)

    def _calculate_points(self, receipt: Receipt) -> int:
        points = 0
        points += len(receipt.retailer.replace(" ", ""))  # Points for retailer name

        if receipt.total.is_integer(): 
            points += 50

        if receipt.total % 0.25 == 0:
            points += 25

        points += (len(receipt.items) // 2) * 5

        for item in receipt.items:
            if len(item['shortDescription'].strip()) % 3 == 0:
                points += round(float(item['price']) * 0.2)

        if receipt.total > 10.00:
            points += 5

        purchase_date = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d")
        if purchase_date.day % 2 == 1:
            points += 6

        purchase_time = datetime.strptime(receipt.purchaseTime, "%H:%M")
        if 14 <= purchase_time.hour < 16:
            points += 10

        return points

    def get_receipt_points(self, receipt_id: str) -> ReceiptPointsSchema:
        if receipt_id in self.receipts:
            return ReceiptPointsSchema(points=self.receipts[receipt_id]['points'])
        else:
            raise ValueError("Receipt not found") 