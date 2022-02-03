from fastapi import FastAPI
from routes import router

app = FastAPI(title= "Dummy API",
    description="Trii challenge",
    version="0.0.1")
app.include_router(router)

@app.get("/health")
async def health():
    return {"status": "UP"}