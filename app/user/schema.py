from typing import List, Optional
from pydantic import EmailStr
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    full_name: str
    password: str
    google_id: Optional[str] = None
    updated_at: Optional[str] = None
    created_at: Optional[str] = None
    payment_verified: Optional[str] = None
    email_verified: Optional[str] = None
    subcription_at: Optional[str] = None
    subscription_expired: Optional[bool] = True
    role: Optional[int] = 2
    
class UserCreate(UserBase):
    pass

class UserLogin(BaseModel):
    email: str
    password: str