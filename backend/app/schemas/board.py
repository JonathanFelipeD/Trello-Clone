from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class BoardCreate(BaseModel):
    name: str
    description: str | None = None

class BoardResponse(BaseModel):
    id: UUID
    name: str
    description: str | None 
    owner_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True

        