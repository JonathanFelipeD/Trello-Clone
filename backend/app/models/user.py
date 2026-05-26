from sqlalchemy import Column, String, Enum, Datetime
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid
import datetime

class User(Base):
    __tablename__ ='users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum("member", "team_leader", "gerneral_leader", name="user_role"), default="member")
    created_at = Column(Datetime, default=datetime.datetime.now(datetime.timezone.utc))
