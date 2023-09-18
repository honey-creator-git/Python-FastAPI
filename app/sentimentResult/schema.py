from typing import Optional
from pydantic import  BaseModel

class SentimentResult(BaseModel):
    keyword: str
    label: str
    score: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None