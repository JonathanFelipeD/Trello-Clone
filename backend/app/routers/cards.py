from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.card import Card
from app.models.list import List
from app.models.board import Board
from app.schemas.card import CardCreate, CardResponse
from typing import List as TypingList
from uuid import UUID
import jwt
import os
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter(prefix="/lists/{list_id}/cards", tags=["cards"])
security = HTTPBearer()

def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
    return payload.get("sub")

@router.post("/", response_model=CardResponse)
def create_card(list_id: UUID, card_data: CardCreate, db: Session = Depends(get_db), user_id: str = Depends(get_current_user_id)):
    list_obj = db.query(List).filter(List.id == list_id).first()
    if not list_obj:
        raise HTTPException(status_code=404, detail="Lista não encontrada")
    new_card = Card(
        list_id=list_id,
        title=card_data.title,
        description=card_data.description,
        position=card_data.position,
        priority=card_data.priority,
        due_date=card_data.due_date
    )
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card

@router.get("/", response_model=TypingList[CardResponse])
def get_cards(list_id: UUID, db: Session = Depends(get_db), user_id: str = Depends(get_current_user_id)):
    list_obj = db.query(List).filter(List.id == list_id).first()
    if not list_obj:
        raise HTTPException(status_code=404, detail="Lista não encontrada")
    cards = db.query(Card).filter(Card.list_id == list_id).all()
    return cards