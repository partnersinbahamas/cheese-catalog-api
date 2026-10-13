from fastapi import FastAPI, Depends, HTTPException

import schemas
import crud
from db import models
from db.engine import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_cheese_type_by_name(db: SessionLocal, name: str):
    return db.query(models.DBCheeseType).filter(models.DBCheeseType.name == name).first()


def get_cheese_by_title_and_type(db: SessionLocal, title: str, cheese_type_id: int):
    return db.query(models.DBCheese).filter(models.DBCheese.title == title, models.DBCheese.cheese_type_id == cheese_type_id).first()

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
    if get_cheese_type_by_name(db, cheese_type.name):
        raise HTTPException(status_code=400, detail="Cheese type already exists")
    return crud.create_cheese_type(db, cheese_type)


@app.get("/cheese/", response_model=list[schemas.CheeseRead])
def get_cheese(db: SessionLocal = Depends(get_db)):
    return crud.get_cheese_all(db)


@app.post("/cheese/", response_model=schemas.CheeseRead)
def create_cheese(cheese: schemas.CheeseCreate, db:SessionLocal = Depends(get_db)):
    if get_cheese_by_title_and_type(db, cheese.title, cheese.cheese_type_id):
        raise HTTPException(status_code=400, detail="Cheese with this title ans cheese type already exists")
    return crud.create_cheese(db, cheese)
