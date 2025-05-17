from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

from interfaces.chatinterfaces import InputMessage

client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1")

app = FastAPI()

@app.get("/")
def index():
    return {"message": "API is running"}

@app.post("/ai-chat")
def aiChat(data: InputMessage):
    data = data.model_dump()
    print("Mensaje:"+ data["message"])
    return {"status": "ok"} 