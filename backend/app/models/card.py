from sqlalchemy import Column, String, Text, Integer, Enum, DateTime, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid
import datetime

class Card(Base):
    __tablename__ = "cards"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    list_id = Column(UUID(as_uuid=True), ForeignKey("lists.id"), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    position = Column(Integer, nullable=False, default=0)
    priority = Column(Enum("low", "medium", "high", name="card_priority"), default="medium")
    assigned_to = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    due_date = Column(Date, nullable=True)
    status = Column(Enum("todo", "in_progress", "done", name="card_status"), default="todo")
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))