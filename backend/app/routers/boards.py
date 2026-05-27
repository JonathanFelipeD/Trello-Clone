from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.board import Board
from app.schemas.board import BoardCreate, BoardResponse
from typing import List
import jwt
import os
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


router = APIRouter(prefix="/boards", tags=["boards"])
security = HTTPBearer()

def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials # type: ignore
    playload = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
    return playload.get("sub")

@router.post("/", response_model=BoardResponse)
def create_board(board: BoardCreate, db: Session = Depends(get_db), user_id: str = Depends(get_current_user_id)):
    new_board = Board(
        name=board.name,
        description=board.description,
        owner_id=user_id
    )
    db.add(new_board)
    db.commit()
    db.refresh(new_board)
    return new_board

@router.get("/", response_model=List[BoardResponse])
def get_boards(db: Session = Depends(get_db), user_id: str = Depends(get_current_user_id)):
    boards = db.query(Board).filter(Board.owner_id == user_id).all()
    return boards
