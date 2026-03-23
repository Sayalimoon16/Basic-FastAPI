from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="My First API",
    description="Basic FastAPI project for learning",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome Sayali 🚀",
        "status": "success"
    }

@app.get("/hello")
def hello(name: str = "User"):
    return {
        "message": f"Hello, {name} 👋",
        "time": datetime.now()
    }

@app.get("/health")
def health_check():
    return {
        "status": "API is running perfectly ✅"
    }