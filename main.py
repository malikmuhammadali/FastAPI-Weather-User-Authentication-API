from fastapi import FastAPI
import models
from database import engine
from auth import router as auth_router
from weather import router as weather_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Task")

app.include_router(auth_router)
app.include_router(weather_router)

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Task API"}
