from fastapi import FastAPI, Depends

import schemas
import crud
from db.engine import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/cheese-types/", response_model=list[schemas.CheeseTypeRead])
def get_cheese_types(db: SessionLocal = Depends(get_db)):
    return crud.get_cheese_type_all(db)

@app.post("/cheese-types/", response_model=schemas.CheeseTypeRead)
def create_cheese_type(
        cheese_type: schemas.CheeseTypeCreate,
        db: SessionLocal = Depends(get_db)
):
    return crud.create_cheese_type(db, cheese_type)
