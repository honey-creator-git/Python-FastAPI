from typing import Optional
from pydantic import BaseModel

class Messaging(BaseModel):
    messaging: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None