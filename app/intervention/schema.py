from typing import Optional
from pydantic import BaseModel

class HandleIntervention(BaseModel):
    information: str
    additional_information: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None