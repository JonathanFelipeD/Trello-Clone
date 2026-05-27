from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, boards

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(boards.router)

@app.get("/")
def root():
    return {"message" : "Trello Clone API"}