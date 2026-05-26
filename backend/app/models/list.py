from sqlalchemy import Column, String, Integer, Datetime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid
import datetime

class List(Base):
    __tablename__ = "lists"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    board_id = Column(UUID(as_uuid=True), ForeignKey("boards.id"), nullable=False)
    name = Column(String(100), nullable=False)
    position = Column(Integer, nullable=False, default=0)
    created_at = Column(Datetime, default=datetime.datetime.now(datetime.timezone.utc))