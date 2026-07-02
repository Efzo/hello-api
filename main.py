from fastapi import FastAPI
from app.routers import tasks


app = FastAPI(
    title =  "Hello API",
    description = " FastAPI mini project",
    version = "0.1.0",   
)


app.include_router(tasks.router)


@app.get("/health")
async def health_check():
    return {"status": "ok"}





