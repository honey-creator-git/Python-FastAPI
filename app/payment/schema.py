from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    user_id: int
    amount: int
    currency_type: str
    payment_type: str
    status: str
    created_at: Optional[str] = None
    
class PaymentLog(PaymentBase):
    pass
    
class CheckOut(BaseModel):
    amount: int
