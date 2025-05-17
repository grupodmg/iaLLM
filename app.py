from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import aiRouter

app = FastAPI()
app.include_router(aiRouter.router)

@app.get("/")
def index():
    return {"message": "API is running"}