from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class ListCreate(BaseModel):
    name: str
    position: int = 0

class ListResponse(BaseModel):
    id: UUID
    board_id: UUID
    name: str
    position: int
    created_at: datetime

    class Config:
        from_attributes = True