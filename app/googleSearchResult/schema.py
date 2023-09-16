from typing import Optional
from pydantic import BaseModel

class GoogleSearchResult(BaseModel):
    search_id: str
    title: str
    link: str
    snippet: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None