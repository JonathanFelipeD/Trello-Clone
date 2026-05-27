from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, date
from typing import Optional

class CardCreate(BaseModel):
    title: str
    description: Optional[str] = None
    position: int = 0
    priority: str = "medium"
    due_date: Optional[date] = None

class CardResponse(BaseModel):
    id: UUID
    list_id: UUID
    title: str
    description: Optional[str]
    position: int
    priority: str
    assigned_to: Optional[UUID]
    due_date: Optional[date]
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True