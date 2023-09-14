from typing import Optional
from pydantic import EmailStr
from pydantic import BaseModel

class UserBase(BaseModel):
    email: Optional[EmailStr]
    full_name: Optional[str]
    password: Optional[str]
    google_id: Optional[str] = None
    updated_at: Optional[str] = None
    created_at: Optional[str] = None
    payment_verified: Optional[str] = None
    email_verified: Optional[str] = None
    subcription_at: Optional[str] = None
    subscription_expired: Optional[int] = None # 1-True 2-False
    role: Optional[int] = 2 # 1-Admin 2-User
    
class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserLogin(BaseModel):
    email: str
    password: str