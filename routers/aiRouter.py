from openai import OpenAI
from fastapi import APIRouter
from interfaces.chatinterfaces import InputMessage

router = APIRouter()

client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1")


@router.post("/ai-chat")
def aiChat(data: InputMessage):
    data = data.model_dump()
    print("Mensaje:"+ data["message"])

    message= "Por favor respode de manera correcta y concisa a la siguiente pregunta: "

    try:
        completion = client.chat.completions.create(
            model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un asistente de IA que responde de forma corta preguntas en español."
                },
                {
                    "role": "user",
                    "content": message + "Responde a esta pregunta: " + data["message"]
                }
            ],
        )
        response_text = getattr(completion.choices[0].message, "content", "")
        print("response: " + response_text)
        return {"status": "ok", "response": response_text}
    
    except Exception as e:
        print("Error en la API de OpenAI:", e)
        return {"error": f"Error en la API de OpenAI: {str(e)}"}