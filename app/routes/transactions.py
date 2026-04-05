
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter(prefix="/transactions", tags=["Transactions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.TransactionResponse, summary="Create Transaction")
def create(data: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, data)

@router.get("/", response_model=list[schemas.TransactionResponse], summary="Get Transactions")
def read(type: str = Query(None), category: str = Query(None), db: Session = Depends(get_db)):
    return crud.get_transactions(db, type, category)

@router.put("/{id}", summary="Update Transaction")
def update(id: int, data: schemas.TransactionCreate, db: Session = Depends(get_db)):
    obj = crud.update_transaction(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return obj

@router.delete("/{id}", summary="Delete Transaction")
def delete(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_transaction(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"message": "Deleted successfully"}
