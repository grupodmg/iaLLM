from openai import OpenAI
from fastapi import APIRouter
from interfaces.chatinterfaces import InputMessage

router = APIRouter()

client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1")

@app.post("/ai-chat")
def aiChat(data: InputMessage):
    data = data.model_dump()
    print("Mensaje:"+ data["message"])
    return {"status": "ok"} 