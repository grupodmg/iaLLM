from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import aiRouter

app = FastAPI()
app.include_router(aiRouter.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"message": "API is running"}