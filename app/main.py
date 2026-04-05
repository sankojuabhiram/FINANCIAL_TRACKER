
from fastapi import FastAPI
from app.database import Base, engine
from app.routes import transactions, analytics, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance System Backend")

@app.get("/")
def home():
    return {"message": "Finance Backend Running"}

app.include_router(transactions.router)
app.include_router(analytics.router)
app.include_router(users.router)
