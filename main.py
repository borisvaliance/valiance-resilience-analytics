from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="NFIRS AI API")

@app.get("/health")
def health():
    """Simple health check endpoint"""
    return {
        "status": "ok",
        "ai_provider": os.getenv("AI_PROVIDER", "azure"),
        "db": os.getenv("NFIRS_DB_URL", "unset"),
    }

@app.get("/")
def home():
    return {"message": "Welcome to the NFIRS AI API"}
