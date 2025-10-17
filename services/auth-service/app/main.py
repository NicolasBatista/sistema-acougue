from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI(title="Auth Service")

@app.get("/ping")
async def ping():
    return {"message": "pong"}

app.include_router(api_router)
