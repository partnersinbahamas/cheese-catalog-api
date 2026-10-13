import schemas

from sqlalchemy.orm import Session
from db import models
from db.models import PackagingType


def get_cheese_type_all(db: Session):
    return db.query(models.DBCheeseType).all()


def create_cheese_type(db: Session, cheese_type: schemas.CheeseTypeCreate):
    db_cheese_type = models.DBCheeseType(**cheese_type.model_dump())
    db.add(db_cheese_type)
    db.commit()

    db.refresh(db_cheese_type)
    return db_cheese_type


def get_cheese_all(
    db: Session,
    packaging_type: PackagingType | None,
    cheese_title: str | None,
    cheese_type: str | None

):
    queryset = db.query(models.DBCheese)

    if packaging_type is not None:
        queryset = queryset.filter(models.DBCheese.packaging_type == packaging_type.value)

    if cheese_title is not None:
        queryset = queryset.filter(models.DBCheese.title.contains(cheese_title))

    if cheese_type is not None:
        queryset = queryset.filter(models.DBCheese.cheese_type.has(name=cheese_type))

    return queryset.all()


def create_cheese(db: Session, cheese: schemas.CheeseCreate):
    db_cheese = models.DBCheese(**cheese.model_dump())
    db.add(db_cheese)
    db.commit()

    db.refresh(db_cheese)
    return db_cheese


def get_cheese_by_id(db: Session, cheese_id: int):
    return db.query(models.DBCheese).filter(models.DBCheese.id == cheese_id).first()
