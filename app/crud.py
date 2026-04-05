
from sqlalchemy.orm import Session
from app import models

def create_transaction(db: Session, data):
    obj = models.Transaction(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_transactions(db: Session, type=None, category=None):
    query = db.query(models.Transaction)
    if type:
        query = query.filter(models.Transaction.type == type)
    if category:
        query = query.filter(models.Transaction.category == category)
    return query.all()

def update_transaction(db: Session, id: int, data):
    obj = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if obj:
        for key, value in data.dict().items():
            setattr(obj, key, value)
        db.commit()
        db.refresh(obj)
    return obj

def delete_transaction(db: Session, id: int):
    obj = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
