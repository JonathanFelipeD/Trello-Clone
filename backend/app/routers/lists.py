from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.list import List
from app.schemas.list import ListCreate, ListResponse
from app.models.board import Board
from typing import List as TypingList
import jwt
import os
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter(prefix="/boards/{board_id}/lists", tags=["lists"])
security = HTTPBearer()

def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
    return payload.get("sub")

@router.post("/", response_model=ListResponse)
def create_list(board_id: UUID, list_data: ListCreate, db: Session = Depends(get_db), user_id: str = Depends(get_current_user_id)):
    board = db.query(Board).filter(Board.id == board_id, Board.owner_id == user_id).first()
    if not board:
        raise HTTPException(status_code=404, detail="Board não encontrado")
    new_list = List(
        board_id=board_id,
        name=list_data.name,
        position=list_data.position
    )
    db.add(new_list)
    db.commit()
    db.refresh(new_list)
    return new_list

@router.get("/", response_model=TypingList[ListResponse])
def get_lists(board_id: UUID, db: Session = Depends(get_db), user_id: str = Depends(get_current_user_id)):
    board = db.query(Board).filter(Board.id == board_id, Board.owner_id == user_id).first()
    if not board:
        raise HTTPException(status_code=404, detail="Board não encontrado")
    lists = db.query(List).filter(List.board_id == board_id).all()
    return lists