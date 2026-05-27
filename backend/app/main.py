from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, boards, lists, cards

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(boards.router)
app.include_router(lists.router)
app.include_router(cards.router)

@app.get("/")
def root():
    return {"message" : "Trello Clone API"}