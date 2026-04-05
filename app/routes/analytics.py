
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

router = APIRouter(prefix="/analytics", tags=["Analytics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/summary", summary="Financial Summary")
def summary(db: Session = Depends(get_db)):
    tx = db.query(models.Transaction).all()
    income = sum(t.amount for t in tx if t.type == "income")
    expense = sum(t.amount for t in tx if t.type == "expense")

    category_breakdown = {}
    for t in tx:
        category_breakdown[t.category] = category_breakdown.get(t.category, 0) + t.amount

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense,
        "category_breakdown": category_breakdown
    }
