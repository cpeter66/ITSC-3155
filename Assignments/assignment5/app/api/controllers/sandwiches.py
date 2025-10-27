from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas
from ..models.schemas import SandwichBase


def create(db: Session, sandwich):
    db_sandwich = models.Sandwich(
        sandwich_name = sandwich.sandwich_name,
        price = sandwich.price,
    )
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, sandwichID):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwichID).first()

def update(db: Session, sandwichID, sandwich):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwichID)
    update_data = sandwich.model_dump(exclude_unset=True)
    db_sandwich.update(update_data, synchronize_session=False)
    db.commit()
    return db_sandwich.first()

def delete(db: Session, sandwichID):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwichID)
    db_sandwich.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
